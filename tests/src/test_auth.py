import pytest
from flask.testing import FlaskClient
from loguru import logger
from utils.routes import Rules
from utils.testdata import Testdata


def test_registration(client: FlaskClient, registration):
    _, response = registration
    assert response.status_code == 201


def test_login(client: FlaskClient, login):
    _, response, _ = login
    logger.info(response.json)
    logger.info(response.status)
    assert response.status_code == 200


def test_logout(client: FlaskClient, login):
    access_token, _, _ = login
    response = client.delete(
        Rules.auth_logout.value,
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(access_token),
        },
    )
    assert response.status_code == 200


def test_refresh_token(client: FlaskClient, login):
    _, _, refresh_token = login
    response = client.post(
        Rules.auth_refresh_token.value,
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(refresh_token),
        },
    )

    assert response.status_code == 200


def test_history(client: FlaskClient, login):
    access_token, _, _ = login
    response = client.get(
        Rules.auth_history.value,
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(access_token),
        },
    )
    assert response.status_code == 200


def test_change(client: FlaskClient, login, testdata: Testdata):
    user = testdata.create_user()
    access_token, _, _ = login
    response = client.post(
        Rules.auth_change.value,
        json=user.dict(include={"first_name", "last_name"}),
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(access_token),
        },
    )
    assert response.status_code == 200
