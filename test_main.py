from main import User


def test_user_has_name():

    user = User("A")
    assert user.name == "A"
    assert user.childs == list()


def test_user_has_childs():
    user_a = User("A")
    user_b = User("B")
    user_a.set_childs([user_b])

    assert user_a.childs
    assert len(user_a.childs) == 1
    assert user_a.childs[0] == user_b
