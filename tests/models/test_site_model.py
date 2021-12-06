from tests.fixtures.model_fixture import new_site


def test_new_site(new_site):
    assert new_site.max_power == 9000.9
    assert new_site.name == "Metron Lab"
    assert new_site.uid == "f2971753-cd23-4162-93f4-95375a7c5795"
    assert new_site.address == "2 Rue montmartre, 75002 Paris"
    assert new_site.manager_id == "f2971753-cd23-4162-93f4-95375a7c5746"
    assert new_site.created_at == "2021-12-05 14:57:31.603282"
    assert new_site.updated_at == None
