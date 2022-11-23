
class Employee:
    def __init__(self):
        self.empid = int(input("Enter Employee id : "))
        self.name = input("Enter Employee name : ")
        self.salary = float(input("Enter Employee salary : "))

    def display(self):
        print("Employee id : ", self.empid)
        print("Employee name : ", self.name)
        print("Employee salary : ", self.salary)


# Driver code
e1 = Employee()
e1.display()