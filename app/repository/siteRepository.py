from app.database.models.asset import Asset
from app.database.models.site import Site
from app import db
from sqlalchemy.sql import func

"""
    Site repository
    @created on December 4th 
    @author Mama
"""

session = db.session


class SiteRepository:
    def create_site(self, uid, name, address, max_power, manager_id):
        site = Site(
            uid=uid,
            name=name,
            address=address,
            max_power=max_power,
            manager_id=manager_id,
        )
        session.add(site)
        session.commit()

    def get_site_by_uid(self, uid):
        return session.query(Site).filter(Site.uid == uid).one_or_none()

    def get_all_sites(self):
        return session.query(Site).all()

    def update_site(self, uid, name, address, max_power):
        site = session.query(Site).filter(Site.uid == uid).one_or_none()
        if name is not None:
            site.name = name
        if address is not None:
            site.address = address
        if max_power is not None:
            site.max_power = max_power
        session.commit()

    def delete_site_by_uid(self, uid):
        session.query(Site).filter(Site.uid == uid).delete()
        session.commit()

    def get_site_total_assets_power(self, site_id):
        return (
            session.query(func.sum(Asset.power)).filter(Asset.site_id == site_id).all()
        )
