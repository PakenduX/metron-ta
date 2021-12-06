from tests.fixtures.init_database_fixture import init_database
from tests.fixtures.test_client_fixture import test_client
from tests.fixtures.populate_db_with_manager_fixture import add_managers
import json
from faker import Faker

fake = Faker()


def get_access_token(test_client, init_database, add_managers):
    response = test_client.post(
        "/api/v1/auth/login",
        json={"email": "manager1@metron.com", "password": "1234567"},
    )
    data = json.loads(response.data.decode())
    if response.status_code == 200:
        return data["data"]["access_token"]
    return None


def test_add_new_site(test_client, init_database, add_managers):
    # We first sign in to get an access token
    access_token = get_access_token(
        test_client=test_client, init_database=init_database, add_managers=add_managers
    )
    response = test_client.post(
        "/api/v1/sites/add",
        headers={"authorization": "Bearer " + access_token},
        json={"name": fake.company(), "max_power": 1000, "address": fake.address()},
        follow_redirects=True,
    )
    assert response.status_code == 201
    assert response.data == b""
