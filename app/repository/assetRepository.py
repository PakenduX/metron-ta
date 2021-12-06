from app.database.models.asset import Asset
from app import db

"""
    Asset repository
    @created on December 4th 
    @author Mama
"""

session = db.session


class AssetRepository:
    def create_asset(self, uid, name, asset_type, power, site_id):
        asset = Asset(
            uid=uid,
            name=name,
            asset_type=asset_type,
            power=power,
            site_id=site_id,
        )
        session.add(asset)
        session.commit()

    def get_asset_by_uid(self, uid):
        return session.query(Asset).filter(Asset.uid == uid).one_or_none()

    def get_all_assets(self):
        return session.query(Asset).all()

    def update_asset(self, uid, name, asset_type, power):
        site = session.query(Asset).filter(Asset.uid == uid).one_or_none()
        if name is not None:
            site.name = name
        if asset_type is not None:
            site.asset_type = asset_type
        if power is not None:
            site.power = power
        session.commit()

    def delete_asset_by_uid(self, uid):
        session.query(Asset).filter(Asset.uid == uid).delete()
        session.commit()
