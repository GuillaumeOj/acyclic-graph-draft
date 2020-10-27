class ChildMayNotBeParentOfParent(BaseException):
    pass


class User:
    def __init__(self):
        self.children = set()

    def set_child(self, child):
        for child in child.children:
            if not child._check_children(self):
                raise ChildMayNotBeParentOfParent
        self.children.add(child)

    def _check_children(self, parent):
        for child in self.children:
            if child == parent:
                return False
