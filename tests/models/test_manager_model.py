from tests.fixtures.model_fixture import new_manager


def test_new_manager(new_manager):
    assert new_manager.email == "manager@metron.com"
    assert new_manager.name == "Manager"
    assert new_manager.uid == "f2971753-cd23-4162-93f4-95375a7c5746"
    assert (
        new_manager.password
        == "$argon2id$v=19$m=102400,t=2,p=8$8Jm0ejQe0+ICZlRDPEh/7g$KpsFG7Mlq0BuNlickoor/w"
    )
