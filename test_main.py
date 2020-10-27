import pytest

from main import ChildHasParent
from main import ChildMayNotBeParentOfParent
from main import User


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


def test_user_has_already_a_parent():
    A = User()
    B = User()
    C = User()

    A.set_link(child=B)

    with pytest.raises(ChildHasParent):
        C.set_link(child=B)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()

    assert C.parent is None
    assert C.children == set()


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
