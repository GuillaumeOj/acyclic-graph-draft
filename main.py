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
        cls.referrals.sort(key=lambda ref: ref.referee.id)

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
        if not cls.referrals:
            return None

        left = 0
        right = len(cls.referrals) - 1
        while left <= right:
            middle = (left + right) // 2
            if referee.id < cls.referrals[middle].referee.id:
                right = middle - 1
            elif referee.id > cls.referrals[middle].referee.id:
                left = middle + 1
            else:
                return cls.referrals[middle].referrer


class User:
    def __init__(self, id=None):
        self.id = id
