class CircularRefer(BaseException):
    pass


class RefereeIsAlreadyReferred(BaseException):
    pass


class User:
    def __init__(self):
        self.referrer = None

    def set_referrer(self, referrer):
        if self.referrer:
            raise RefereeIsAlreadyReferred

        try:
            self.check_referrer(referrer)
        except CircularRefer as e:
            raise e

        self.referrer = referrer

    def check_referrer(self, referrer):
        if referrer.referrer == self:
            raise CircularRefer
