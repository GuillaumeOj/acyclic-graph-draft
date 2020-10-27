class ChildMayNotBeParentOfParent(BaseException):
    pass


class User:
    pass

    def __init__(self):
        self.parent = None
        self.children = set()

    def set_link(self, child=None, parent=None):
        if child:
            if child == self.parent:
                raise ChildMayNotBeParentOfParent
            self.children.add(child)
            child.set_link(parent=self)
        if parent:
            self.parent = parent
