class User:
    def __init__(self, name):
        self.name = str(name)
        self.childs = list()

    def __str__(self):
        user_name = f"User {self.name}"
        user_childs = str()
        if self.childs:
            childs_name = [child.name for child in self.childs]
            childs = ",".join(childs_name)
            user_childs += f"\n{self.name}'s childs: {childs}"

        return user_name + user_childs

    def set_childs(self, childs):
        self.childs.extend(childs)


users = [User(i) for i in range(3)]

users[0].set_childs(users[1:-1])

for user in users:
    print(user)
