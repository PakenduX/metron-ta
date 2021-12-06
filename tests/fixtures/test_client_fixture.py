from app import create_app
import pytest


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(True)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
