import asyncio
from typing import Generator, Optional

import pytest
from config.settings import settings
from flask import Flask
from flask.testing import FlaskClient
from loguru import logger
from utils.routes import Rules
from utils.structures import User
from utils.testdata import Testdata

from app import create_app

# @pytest.fixture(scope="session")
# def test_config():
#     config: dict = {}
#     config["SUPER_USER_LOGIN"] = os.environ.get("SUPER_USER_LOGIN")
#     config["SUPER_USER_PASS"] = os.environ.get("SUPER_USER_PASS")
#     return config


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def app() -> Generator[Flask, None, None]:
    app: Flask = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture(scope="session")
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()


@pytest.fixture(scope="session")
def testdata() -> Testdata:
    data = Testdata()
    return data


@pytest.fixture()
def user_create(client, testdata: Testdata) -> User:
    user = testdata.create_user()
    response = client.post(
        "api/v1/users/",
        json=user.dict(exclude={"id"}),
        headers={"content-type": "application/json"},
    )
    return User.parse_raw(response.json)


@pytest.fixture
def registration(client: FlaskClient, testdata: Testdata):
    user = testdata.create_user()
    response = client.post(
        Rules.auth_register.value,
        json=user.dict(exclude={"id"}),
        headers={"content-type": "application/json"},
    )
    resp_json: Optional[dict] = response.get_json()
    if not resp_json:
        assert False, response.status
    user.id = resp_json["user"]
    return user, response


@pytest.fixture
def login(client: FlaskClient, registration):
    user, _ = registration
    response = client.post(
        Rules.auth_login.value,
        json=user.dict(include={"email", "password"}),
        headers={"content-type": "application/json"},
    )

    resp_json = response.json
    access_token = None
    refresh_token = None
    if resp_json:
        access_token = resp_json["access_token"]
        refresh_token = resp_json["refresh_token"]
    return access_token or None, response, refresh_token


@pytest.fixture
def admin_user(client: FlaskClient, registration):
    user, _ = registration
    s_login = settings.super_user_login
    s_pass = settings.super_user_pass
    logger.info("={}-{}=".format(s_login, s_pass))
    # login like superuser
    response = client.post(
        Rules.auth_login.value,
        json=user.dict(include={s_login, s_pass}),
        headers={"content-type": "application/json"},
    )
    logger.info(response)
    resp_json = response.json
    access_token = None
    try:
        access_token = resp_json["access_token"]
    except KeyError:
        raise Exception("Could not login like a superuser. Check you login/password.")

    # add admin role to user
    admin_role_id = 2
    response = client.post(
        Rules.users_roles.value.format(id=user.id),
        json={"ids": [admin_role_id]},
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(access_token),
        },
    )

    return user, access_token
