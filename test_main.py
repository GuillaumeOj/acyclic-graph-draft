import pytest
from main import User
from main import ChildMayNotBeParentOfParent


def test_user_has_name():

    user = User("A")
    assert user.name == "A"
    assert user.childs == list()


def test_user_has_childs():
    user_a = User("A")
    user_b = User("B")
    user_a.set_child(user_b)

    assert user_a.childs
    assert len(user_a.childs) == 1
    assert user_a.childs[0] == user_b


def test_user_is_not_a_parent_of_his_own_parent():
    user_a = User("A")
    user_b = User("B")
    user_a.set_child(user_b)

    with pytest.raises(ChildMayNotBeParentOfParent):
        user_b.set_child(user_a)

    assert len(user_a.childs) == 1
    assert user_b.childs == []
