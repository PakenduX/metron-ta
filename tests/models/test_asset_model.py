from app.constants.asset_types import AssetTypes
from tests.fixtures.model_fixture import new_asset


def test_new_asset(new_asset):
    assert new_asset.power == 1000.9
    assert new_asset.name == "Jarvis"
    assert new_asset.uid == "f2971753-cd23-4162-93f4-95375a7c5799"
    assert new_asset.asset_type == AssetTypes.CHILLER
    assert new_asset.site_id == "f2971753-cd23-4162-93f4-95375a7c5795"
    assert new_asset.created_at == "2021-12-05 14:57:31.603282"
    assert new_asset.updated_at == None
