
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '({}, {})'.format(self.name, self.age)

users = [
    User('A', 20),
    User('B', 30),
    User('C', 25),
]

min_age = min(users, key=lambda u: u.age)
print(min_age)