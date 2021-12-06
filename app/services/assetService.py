from app.repository.assetRepository import AssetRepository

repository = AssetRepository()


class AssetService:
    def create_asset(self, uid, name, asset_type, power, site_id):
        return repository.create_asset(
            uid=uid,
            name=name,
            asset_type=asset_type,
            power=power,
            site_id=site_id,
        )

    def get_asset_by_uid(self, uid):
        return repository.get_asset_by_uid(uid=uid)

    def get_all_assets(self):
        return repository.get_all_assets()

    def update_asset(self, uid, name, asset_type, power):
        return repository.update_asset(
            uid=uid, name=name, asset_type=asset_type, power=power
        )

    def delete_asset_by_uid(self, uid):
        repository.delete_asset_by_uid(uid=uid)
