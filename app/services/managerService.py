from app.repository.managerRepository import ManagerRepository

repository = ManagerRepository()


class ManagerService:
    def create_manager(self, uid, name, email, password):
        return repository.create_manager(
            uid=uid, name=name, email=email, password=password
        )

    def get_manager_by_email(self, email):
        return repository.get_manager_by_email(email=email)

    def get_manager_by_uid(self, uid):
        return repository.get_manager_by_uid(uid=uid)

    def get_all_managers(self):
        return repository.get_all_managers()

    def delete_manager_by_uid(self, uid):
        return repository.delete_manager_by_uid(uid=uid)

    def update_manager(self, uid, email, password, name):
        return repository.update_manager(
            email=email, uid=uid, name=name, password=password
        )
