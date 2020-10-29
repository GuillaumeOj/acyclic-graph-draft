class CircularRefer(BaseException):
    pass


class RefereeIsAlreadyReferred(BaseException):
    pass


class User:
    users = list()

    def __init__(self):
        self.referrer = None
        User.users.append(self)

    def set_referral(self, referrer):
        if self.referrer:
            raise RefereeIsAlreadyReferred
        self.referrer = referrer

    def check_referral(self, referee):
        referrer = self.referrer
        while referrer is not None:
            if referrer == referee:
                raise CircularRefer
            referrer = referrer.referrer
