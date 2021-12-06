from app.repository.siteRepository import SiteRepository

repository = SiteRepository()


class SiteService:
    def create_site(self, uid, name, address, max_power, manager_id):
        return repository.create_site(
            uid=uid,
            name=name,
            address=address,
            max_power=max_power,
            manager_id=manager_id,
        )

    def get_site_by_uid(self, uid):
        return repository.get_site_by_uid(uid=uid)

    def get_all_sites(self):
        return repository.get_all_sites()

    def update_site(self, uid, name, address, max_power):
        return repository.update_site(
            uid=uid, name=name, address=address, max_power=max_power
        )

    def delete_site_by_uid(self, uid):
        repository.delete_site_by_uid(uid=uid)

    def get_site_total_assets_power(self, site_id):
        return repository.get_site_total_assets_power(site_id)
