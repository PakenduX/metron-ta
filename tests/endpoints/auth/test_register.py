from tests.fixtures.init_database_fixture import init_database
from tests.fixtures.test_client_fixture import test_client
import json
from faker import Faker

fake = Faker()


def test_valid_register(test_client, init_database):
    response = test_client.post(
        "/api/v1/auth/register",
        json={
            "email": fake.email(),
            "password": "1234567",
            "name": fake.name(),
        },
    )
    assert response.status_code == 201
    assert response.data == b""


def test_register_with_invalid_email(test_client, init_database):
    response = test_client.post(
        "/api/v1/auth/register",
        json={
            "email": "manager3@metron.",
            "password": "1234567",
            "name": fake.name(),
        },
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "message" in data
    assert "status" in data
    assert data["status"] == "error"
    assert data["message"]["email"][0] == "Not a valid email address."
