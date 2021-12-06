from app.database.models.manager import Manager
from app import db

"""
    Manager repository
    @created on December 4th 
    @author Mama
"""

session = db.session


class ManagerRepository:
    def create_manager(self, uid, name, email, password):
        manager = Manager(uid=uid, name=name, email=email, password=password)
        session.add(manager)
        session.commit()

    def get_manager_by_email(self, email):
        return session.query(Manager).filter(Manager.email == email).one_or_none()

    def get_manager_by_uid(self, uid):
        return session.query(Manager).filter(Manager.uid == uid).one_or_none()

    def get_all_managers(self):
        return session.query(Manager).all()

    def delete_manager_by_uid(self, uid):
        session.query(Manager).filter(Manager.uid == uid).delete()
        session.commit()

    def update_manager(self, uid, email, password, name):
        manager = session.query(Manager).filter(Manager.uid == uid).one_or_none()
        if email is not None:
            manager.email = email
        if password is not None:
            manager.password = password
        if name is not None:
            manager.name = name
        session.commit()
