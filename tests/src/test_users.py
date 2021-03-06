from http import HTTPStatus

from utils.testdata import Testdata


def test_user_create(client, testdata: Testdata):
    user = testdata.create_user()
    response = client.post(
        "api/v1/users/",
        json=user.dict(exclude={"id"}),
        headers={"content-type": "application/json"},
    )
    user.id = response.json["id"]
    assert response.status_code == HTTPStatus.OK
    return user


def test_user_delete(client, testdata: Testdata):
    user = testdata.create_user()
    response = client.delete("api/v1/users/{0}".format(user.id))
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_user_update(client, testdata: Testdata):
    user = testdata.create_user()
    user_updated = testdata.create_user()
    response = client.put(
        "api/v1/users/{0}".format(user.id),
        json=user.dict(exclude={"id"}),
        headers={"content-type": "application/json"},
    )
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_user_get(client, user_create):
    response = client.get("api/v1/users/13")
    assert response.status_code == HTTPStatus.OK
