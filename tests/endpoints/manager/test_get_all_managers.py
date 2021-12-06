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


def test_get_all_managers(test_client, init_database, add_managers):
    access_token = get_access_token(
        test_client=test_client, init_database=init_database, add_managers=add_managers
    )
    response = test_client.get(
        "/api/v1/managers",
        headers={"authorization": "Bearer " + access_token},
        follow_redirects=True,
    )
    data = json.loads(response.data.decode())
    assert isinstance(data["data"], list)
    assert response.status_code == 200
    assert "data" in data
    assert data["status"] == "success"
