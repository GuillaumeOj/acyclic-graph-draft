class ChildMayNotBeParentOfParent(BaseException):
    pass


class ChildHasParent(BaseException):
    pass


class User:
    pass

    def __init__(self):
        self.parent = None
        self.children = set()

    def set_link(self, child=None, parent=None):
        if child:
            if child.parent:
                raise ChildHasParent

            self._check_links(child)

            self.children.add(child)
            child.set_link(parent=self)

        if parent:
            if self.parent:
                raise ChildHasParent
            self.parent = parent

    def _check_links(self, child):
        for user in child.children:
            if user.parent == child:
                raise ChildMayNotBeParentOfParent
