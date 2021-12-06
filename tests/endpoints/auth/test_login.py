from tests.fixtures.init_database_fixture import init_database
from tests.fixtures.test_client_fixture import test_client
from tests.fixtures.populate_db_with_manager_fixture import add_managers
import json


def test_valid_login(test_client, init_database, add_managers):
    """
    GIVEN a Flask application
    WHEN the '/api/v1/auth/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post(
        "/api/v1/auth/login",
        json={"email": "manager1@metron.com", "password": "1234567"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert b"status" in response.data
    assert b"access_token" in response.data
    assert b"refresh_token" in response.data
    assert data["status"] == "success"


def test_login_without_credentials(test_client, init_database, add_managers):
    response = test_client.post("/api/v1/auth/login", json={})
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert b"status" in response.data
    assert b"message" in response.data
    assert data["status"] == "error"
    assert data["message"] == "Veuillez saisir vos identifiants"


def test_login_with_invalid_password(test_client, init_database, add_managers):
    response = test_client.post(
        "/api/v1/auth/login",
        json={"email": "manager1@metron.com", "password": "123456"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert b"status" in response.data
    assert b"message" in response.data
    assert data["status"] == "error"
    assert data["message"] == "Votre mot de passe est incorrect"
