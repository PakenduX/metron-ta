import pytest
from app.database.models.manager import Manager
from app.database.models.site import Site
from app.database.models.asset import Asset
from app.constants.asset_types import AssetTypes


@pytest.fixture(scope="module")
def new_manager():
    manager = Manager(
        uid="f2971753-cd23-4162-93f4-95375a7c5746",
        email="manager@metron.com",
        password="$argon2id$v=19$m=102400,t=2,p=8$8Jm0ejQe0+ICZlRDPEh/7g$KpsFG7Mlq0BuNlickoor/w",
        name="Manager",
    )
    return manager


@pytest.fixture(scope="module")
def new_site():
    site = Site(
        uid="f2971753-cd23-4162-93f4-95375a7c5795",
        name="Metron Lab",
        max_power=9000.9,
        address="2 Rue montmartre, 75002 Paris",
        manager_id="f2971753-cd23-4162-93f4-95375a7c5746",
        created_at="2021-12-05 14:57:31.603282",
    )
    return site


@pytest.fixture(scope="module")
def new_asset():
    asset = Asset(
        uid="f2971753-cd23-4162-93f4-95375a7c5799",
        name="Jarvis",
        power=1000.9,
        asset_type=AssetTypes.CHILLER,
        site_id="f2971753-cd23-4162-93f4-95375a7c5795",
        created_at="2021-12-05 14:57:31.603282",
    )
    return asset
