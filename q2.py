class User:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, "+ self.name + "!")

user1 = User("addy")
user1.greet()