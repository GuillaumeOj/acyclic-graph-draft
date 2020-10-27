class ChildMayNotBeParentOfParent(BaseException):
    pass


class User:
    def __init__(self, name):
        self.name = name
        self.childs = list()

    def __str__(self):
        user_name = f"User {self.name}"
        user_childs = str()
        if self.childs:
            childs_name = [child.name for child in self.childs]
            childs = ",".join(childs_name)
            user_childs += f"\n{self.name}'s childs: {childs}"

        return user_name + user_childs

    def set_child(self, child):
        for child in child.childs:
            if child.name == self.name:
                raise ChildMayNotBeParentOfParent
        self.childs.append(child)
