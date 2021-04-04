import pytest

from main import CircularRefer
from main import RefereeIsAlreadyReferred
from main import Referral
from main import User


@pytest.fixture
def referrals():
    Referral.referrals = list()
    yield


def test_referrals(referrals):
    A = User(0)
    B = User(1)

    Referral().set_referral(referee=B, referrer=A)

    assert len(Referral.referrals) == 1


def test_user_refer_a_referrer_with_referees(referrals):
    A = User(0)
    B = User(1)
    C = User(2)

    Referral().set_referral(referee=B, referrer=A)
    Referral().set_referral(referee=A, referrer=C)

    assert len(Referral.referrals) == 2


def test_user_refer_a_user_with_referrer(referrals):
    A = User(0)
    B = User(1)
    C = User(2)

    Referral().set_referral(referee=B, referrer=A)

    with pytest.raises(RefereeIsAlreadyReferred):
        Referral().set_referral(referee=B, referrer=C)

    assert len(Referral.referrals) == 1


def test_user_refer_his_referrer(referrals):
    A = User(0)
    B = User(1)

    Referral().set_referral(referee=B, referrer=A)

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=A, referrer=B)

    assert len(Referral.referrals) == 1


def test_circular_refer_with_four_levels(referrals):
    A = User(0)
    B = User(1)
    C = User(2)
    D = User(3)

    users = [A, B, C, D]

    Referral().set_referral(referee=B, referrer=A)
    Referral().set_referral(referee=C, referrer=B)
    Referral().set_referral(referee=D, referrer=C)

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=A, referrer=D)

    assert len(Referral.referrals) == len(users) - 1


def test_circular_refer_with_thousand_levels(referrals):
    users = [User(i) for i in range(1000)]
    [
        Referral().set_referral(referee=users[i + 1], referrer=users[i])
        for i in range(len(users))
        if i < len(users) - 1
    ]

    with pytest.raises(CircularRefer):
        Referral().set_referral(referee=users[0], referrer=users[-1])
