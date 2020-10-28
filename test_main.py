import pytest

from main import RefereeIsAlreadyReferred
from main import CircularRefer
from main import User


def test_user():
    A = User()
    assert A.referrer is None
    assert A.referees == set()


def test_referrer_has_referees():
    A = User()
    B = User()

    A.set_referral(referee=B)

    assert A.referrer is None
    assert A.referees == {B}

    assert B.referrer == A
    assert B.referees == set()


def test_user_refer_a_referrer_with_referees():
    A = User()
    B = User()
    C = User()

    A.set_referral(referee=B)
    C.set_referral(referee=A)

    assert A.referrer == C
    assert A.referees == {B}

    assert B.referrer == A
    assert B.referees == set()

    assert C.referrer is None
    assert C.referees == {A}


def test_user_refer_a_user_with_referrer():
    A = User()
    B = User()
    C = User()

    A.set_referral(referee=B)

    with pytest.raises(RefereeIsAlreadyReferred):
        C.set_referral(referee=B)

    assert A.referrer is None
    assert A.referees == {B}

    assert B.referrer == A
    assert B.referees == set()

    assert C.referrer is None
    assert C.referees == set()


def test_user_refer_his_referrer():
    A = User()
    B = User()

    A.set_referral(referee=B)

    with pytest.raises(CircularRefer):
        B.set_referral(referee=A)

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

    A.set_referral(referee=B)
    B.set_referral(referee=C)
    C.set_referral(referee=D)

    with pytest.raises(CircularRefer):
        D.set_referral(referee=A)

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
        users[i].set_referral(referee=users[i + 1])
        for i in range(len(users))
        if i < len(users) - 1
    ]

    with pytest.raises(CircularRefer):
        users[-1].set_referral(referee=users[0])
