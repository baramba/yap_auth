import pytest
from flask.testing import FlaskClient
from loguru import logger
from utils.routes import Rules

from tests.utils.testdata import Testdata


def test_permissions_add(client: FlaskClient, admin_user, testdata: Testdata):
    admin, access_token = admin_user
    response = client.post(
        Rules.permissions_post.value,
        json=testdata.gen_permission().dict(exclude={"id"}),
        headers={
            "content-type": "application/json",
            "Authorization": "Bearer {0}".format(access_token),
        },
    )
    assert response.status_code == 200
