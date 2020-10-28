class ChildMayNotBeParentOfParent(BaseException):
    pass


class ChildHasParent(BaseException):
    pass


class User:
    def __init__(self):
        self.parent = None
        self.children = set()

    def set_link(self, child=None, parent=None):
        if child:
            if child.parent:
                raise ChildHasParent

            self.check_link(child)

            self.children.add(child)
            child.set_link(parent=self)

        if parent:
            if self.parent:
                raise ChildHasParent
            self.parent = parent

    def check_link(self, child):
        parent = self.parent
        while parent is not None:
            if parent == child:
                raise ChildMayNotBeParentOfParent
            parent = parent.parent
