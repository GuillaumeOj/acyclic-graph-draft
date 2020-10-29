import pytest

from main import RefereeIsAlreadyReferred
from main import CircularRefer
from main import User
from main import Referral


@pytest.fixture
def referrals():
    Referral.referrals = list()
    yield


def test_referrals(referrals):
    A = User()
    B = User()

    Referral().set_referral(referee=B, referrer=A)

    assert Referral.referrals[0].referee == B
    assert Referral.referrals[0].referrer == A
    assert len(Referral.referrals) == 1


def test_user_refer_a_referrer_with_referees(referrals):
    A = User()
    B = User()
    C = User()

    Referral().set_referral(referee=B, referrer=A)
    Referral().set_referral(referee=A, referrer=C)

    assert len(Referral.referrals) == 2

    assert Referral.referrals[0].referee == B
    assert Referral.referrals[0].referrer == A

    assert Referral.referrals[1].referee == A
    assert Referral.referrals[1].referrer == C


def test_user_refer_a_user_with_referrer(referrals):
    A = User()
    B = User()
    C = User()

    Referral().set_referral(referee=B, referrer=A)

    with pytest.raises(RefereeIsAlreadyReferred):
        Referral().set_referral(referee=B, referrer=C)

    assert len(Referral.referrals) == 1

    assert Referral.referrals[0].referee == B
    assert Referral.referrals[0].referrer == A


def test_user_refer_his_referrer(referrals):
    A = User()
    B = User()

    Referral().set_referral(referee=B, referrer=A)

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=A, referrer=B)

    assert len(Referral.referrals) == 1

    assert Referral.referrals[0].referee == B
    assert Referral.referrals[0].referrer == A


def test_circular_refer_with_four_levels(referrals):
    A = User("A")
    B = User("B")
    C = User("C")
    D = User("D")

    users = [A, B, C, D]

    Referral().set_referral(referee=B, referrer=A)
    Referral().set_referral(referee=C, referrer=B)
    Referral().set_referral(referee=D, referrer=C)

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=A, referrer=D)

    assert len(Referral.referrals) == len(users) - 1

    for i, referral in enumerate(Referral.referrals):
        assert referral.referee == users[i + 1]
        assert referral.referrer == users[i]


def test_circular_refer_with_thousand_levels(referrals):
    users = [User() for _ in range(1000)]

    [
        Referral().set_referral(referee=users[i + 1], referrer=users[i])
        for i in range(len(users))
        if i < len(users) - 1
    ]

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=users[0], referrer=users[-1])
