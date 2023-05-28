# Structure ---> User Defined Datatype

# Limitations: 1. BY default Public, 2. We can't add methods with the variables

# class student
# {
#     int id;
#     float marks;
#     char name[10];

#     void set_marks()
#     {

#     }

#     void display()
#     {
        
#     }
# };


# class - Bluecopy
# object - Instance
# Constructor ---> TO solve Intialization Problem  (Auto - calling)
# Student()
# {

# }


class Student:
    id = 30  # Class Variable

    def __init__(self):
        self.name = "Krutarth"   # Instance Member Variable
        self.marks = 90
        self.address = "Ahm"

    def show_details(self):  # Instance Method
        print(self.name, self.marks, self.address,Student.id)


# Student s1;
diya = Student()
priyank = Student()

diya.name = "Diya"
diya.marks = 500

diya.show_details()
priyank.show_details()



# ---------------------------------------------------
# self ---> this keyword (in CPP)

class Bank():
    ROI = 4   # class variable

    def __init__(self, name):
        self.balance = 0
        self.name = name

    def add_money(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_bal(self):
        print(self.name, self.balance)


krutarth = Bank("Krutarth")
hemal = Bank("Hemal")

krutarth.id = 90   # Make Variable from outside of class

print(krutarth.id)  # 90

krutarth.add_money(1000)
krutarth.check_bal()
hemal.check_bal()

print(krutarth.ROI)  # 4

# hemal.ROI = 9
# print(krutarth.ROI)  # 4
# print(hemal.ROI)  # 9
# print(Bank.ROI)  # 4

Bank.ROI = 18

print(krutarth.ROI)  # 18
print(hemal.ROI)   # 18