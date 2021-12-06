import pytest
from app import db


@pytest.fixture(scope="module")
def init_database():
    db.create_all()
    yield db
