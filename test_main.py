import pytest

from main import RefereeIsAlreadyReferred
from main import CircularRefer
from main import User


def test_user():
    A = User()
    assert A.referrer is None


def test_referrer_has_referees():
    A = User()
    B = User()

    B.set_referrer(A)

    assert A.referrer is None

    assert B.referrer == A


def test_user_refer_a_referrer_with_referees():
    A = User()
    B = User()
    C = User()

    B.set_referrer(A)
    A.set_referrer(C)

    assert A.referrer == C
    assert B.referrer == A
    assert C.referrer is None


def test_user_refer_a_user_with_referrer():
    A = User()
    B = User()
    C = User()

    B.set_referrer(A)

    with pytest.raises(RefereeIsAlreadyReferred):
        B.set_referrer(C)

    assert A.referrer is None

    assert B.referrer == A

    assert C.referrer is None


def test_user_refer_his_referrer():
    A = User()
    B = User()

    A.set_referrer(referee=B)

    with pytest.raises(CircularRefer):
        B.set_referrer(referee=A)

    assert A.referrer is None
    assert A.referees == {B}

    assert B.referrer == A
    assert B.referees == set()


def test_circular_refer():
    # more than 3 levels
    A = User()
    B = User()
    C = User()
    D = User()

    A.set_referrer(referee=B)
    B.set_referrer(referee=C)
    C.set_referrer(referee=D)

    with pytest.raises(CircularRefer):
        D.set_referrer(referee=A)

    assert A.referrer is None
    assert A.referees == {B}

    assert B.referrer == A
    assert B.referees == {C}

    assert C.referrer == B
    assert C.referees == {D}

    assert D.referrer == C
    assert D.referees == set()

    # many levels
    users = [User() for _ in range(1000)]

    [
        users[i].set_referrer(referee=users[i + 1])
        for i in range(len(users))
        if i < len(users) - 1
    ]

    with pytest.raises(CircularRefer):
        users[-1].set_referrer(referee=users[0])
