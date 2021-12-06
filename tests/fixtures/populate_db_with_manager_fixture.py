import pytest
from app import db
from app.database.models.manager import Manager


@pytest.fixture(scope="module")
def add_managers():
    manager_1 = Manager(
        uid="f2971753-cd23-4162-93f4-95375a7c5746",
        email="manager1@metron.com",
        password="$argon2id$v=19$m=102400,t=2,p=8$07cdKblN9QO9570sepFjjQ$UtLjB/e5toqAfeGTKDL9cQ",
        name="Manager1",
    )
    manager_2 = Manager(
        uid="f2971753-cd23-4162-93f4-95375a7c5747",
        email="manager2@metron.com",
        password="$argon2id$v=19$m=102400,t=2,p=8$07cdKblN9QO9570sepFjjQ$UtLjB/e5toqAfeGTKDL9cQ",
        name="Manager2",
    )
    db.session.add(manager_1)
    db.session.add(manager_2)
    db.session.commit()
    yield manager_1, manager_2
    # I delete the added managers just after to keep the db clean
    db.session.query(Manager).filter(Manager.uid == manager_1.uid).delete()
    db.session.query(Manager).filter(Manager.uid == manager_2.uid).delete()
    db.session.commit()
