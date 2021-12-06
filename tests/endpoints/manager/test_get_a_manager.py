from tests.fixtures.init_database_fixture import init_database
from tests.fixtures.test_client_fixture import test_client
from tests.fixtures.populate_db_with_manager_fixture import add_managers
import json


def get_access_token(test_client, init_database, add_managers):
    response = test_client.post(
        "/api/v1/auth/login",
        json={"email": "manager1@metron.com", "password": "1234567"},
    )
    data = json.loads(response.data.decode())
    if response.status_code == 200:
        return data["data"]["access_token"]
    return None


def test_get_manager_by_email(test_client, init_database, add_managers):
    access_token = get_access_token(
        test_client=test_client, init_database=init_database, add_managers=add_managers
    )
    response = test_client.get(
        "/api/v1/managers/manager1@metron.com",
        headers={"authorization": "Bearer " + access_token},
        follow_redirects=True,
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "data" in data
    assert data["status"] == "success"
    assert data["data"]["email"] == "manager1@metron.com"
    assert data["data"]["name"] == "Manager1"


def test_get_non_existant_manager_by_email(test_client, init_database, add_managers):
    access_token = get_access_token(
        test_client=test_client, init_database=init_database, add_managers=add_managers
    )
    response = test_client.get(
        "/api/v1/managers/manager1@metron.co",
        headers={"authorization": "Bearer " + access_token},
        follow_redirects=True,
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 404
    assert data["status"] == "error"
    assert data["message"] == "Aucun manager avec cet email"
