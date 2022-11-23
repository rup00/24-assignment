class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def print_user(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Email: ", self.email)


user1 = User("John", 25, "john@example.com")
user1.print_user()