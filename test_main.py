import pytest
from main import User
from main import ChildMayNotBeParentOfParent


def test_user_has_name():

    A = User()
    assert A.parent is None
    assert A.children == set()


def test_user_has_children():
    A = User()
    B = User()

    A.set_link(child=B)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()


def test_user_is_not_parent_of_his_own_parent():
    A = User()
    B = User()

    A.set_link(child=B)

    with pytest.raises(ChildMayNotBeParentOfParent):
        B.set_link(child=A)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()
