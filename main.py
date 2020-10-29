class CircularRefer(BaseException):
    pass


class RefereeIsAlreadyReferred(BaseException):
    pass


class Referral:
    referrals = list()

    def __init__(self):
        self.referrer = None
        self.referee = None

    def set_referral(self, referee, referrer):
        try:
            self.check_referral(referee, referrer)
        except Exception as e:
            raise e

        self.referee = referee
        self.referrer = referrer

        self.add_referral(self)

    @classmethod
    def add_referral(cls, referral):
        cls.referrals.append(referral)

    def check_referral(self, referee, referrer):
        if self.get_referrer(referee):
            raise RefereeIsAlreadyReferred

        previous_referrer = self.get_referrer(referrer)
        while previous_referrer:
            if previous_referrer == referee:
                raise CircularRefer
            previous_referrer = self.get_referrer(previous_referrer)

    @classmethod
    def get_referrer(cls, referee):
        for referral in cls.referrals:
            if referral.referee == referee:
                return referral.referrer


class User:
    def __init__(self, id=None):
        self.id = id
