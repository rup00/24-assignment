class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

user1 = User("John", 25, "Male")
user2 = User("Jane", 30, "Female")

print(user1.__dict__)
print(user2.__dict__)