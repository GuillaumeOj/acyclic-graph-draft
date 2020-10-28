class CircularRefer(BaseException):
    pass


class RefereeIsAlreadyReferred(BaseException):
    pass


class User:
    def __init__(self):
        self.referrer = None
        self.referees = set()

    def set_referral(self, referee=None, referrer=None):
        if referee:
            if referee.referrer:
                raise RefereeIsAlreadyReferred

            self.check_referral(referee)

            self.referees.add(referee)
            referee.set_referral(referrer=self)

        if referrer:
            if self.referrer:
                raise RefereeIsAlreadyReferred
            self.referrer = referrer

    def check_referral(self, referee):
        referrer = self.referrer
        while referrer is not None:
            if referrer == referee:
                raise CircularRefer
            referrer = referrer.referrer
