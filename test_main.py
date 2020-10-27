import pytest
from main import User
from main import ChildMayNotBeParentOfParent


def test_user_has_name():

    user = User()
    assert user.children == set()


def test_user_has_children():
    user_a = User()
    user_b = User()

    user_a.set_child(user_b)

    assert user_a.children
    assert len(user_a.children) == 1
    assert user_a.children == {user_b}


def test_user_is_not_a_parent_of_his_own_parent():
    user_a = User()
    user_b = User()
    user_a.set_child(user_b)

    with pytest.raises(ChildMayNotBeParentOfParent):
        user_b.set_child(user_a)

    assert len(user_a.children) == 1
    assert user_b.children == set()


def test_user_is_not_a_parent_of_the_parent_of_his_own_parent():
    users = [User() for _ in range(1000)]

    [users[i].set_child(users[i + 1]) for i in range(len(users) - 1)]

    with pytest.raises(ChildMayNotBeParentOfParent):
        users[-1].set_child(users[0])

    for i in range(len(users) - 1):
        assert len(users[i].children) == 1

    assert users[-1].children == set()
