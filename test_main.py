import pytest

from main import ChildHasParent
from main import ChildMayNotBeParentOfParent
from main import User


def test_user():
    A = User()
    assert A.parent is None
    assert A.children == set()


def test_parent_has_children():
    A = User()
    B = User()

    A.set_link(child=B)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()


def test_user_link_a_parent_with_children():
    A = User()
    B = User()
    C = User()

    A.set_link(child=B)
    C.set_link(child=A)

    assert A.parent == C
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()

    assert C.parent is None
    assert C.children == {A}


def test_user_link_a_user_with_parent():
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


def test_user_link_his_parent():
    A = User()
    B = User()

    A.set_link(child=B)

    with pytest.raises(ChildMayNotBeParentOfParent):
        B.set_link(child=A)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()


def test_user_link_a_parent_of_parent():
    # more than 3 levels
    A = User()
    B = User()
    C = User()
    D = User()

    A.set_link(child=B)
    B.set_link(child=C)
    C.set_link(child=D)

    with pytest.raises(ChildMayNotBeParentOfParent):
        D.set_link(child=A)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == {C}

    assert C.parent == B
    assert C.children == {D}

    assert D.parent == C
    assert D.children == set()

    # many levels
    users = [User() for _ in range(1000)]

    [
        users[i].set_link(child=users[i + 1])
        for i in range(len(users))
        if i < len(users) - 1
    ]

    with pytest.raises(ChildMayNotBeParentOfParent):
        users[-1].set_link(child=users[0])
