# Constructor
# Constructor is basically a special function which has No return type
# To solve Intialization Problem
# Automatically called


# Variables -> 
# 1. Instance Variable 
# 2. Static Variable / class Variable

class Animal:
    legs = 4   # static varibale / class variable
    # def __init__(self):
    #     print("Default Constructor Automatically called")

    def __init__(self,id, name):
        self.eyes = 0
        self.id1 = id   # Instance variable
        self.name1 = name
        print(self.id1,"->",self.name1)


# id1, name1 -> Instance Varibale

# a1 = Animal()   # a1 is object of Animal class
a2 = Animal(100, "Manish")   # 100 -> Manish
a3 = Animal(200, "Shrey")

print(a3.name1)  # Shrey

print(a2.id1 + a3.id1)  # 300
print(a2.name1 + a3.name1)  # 300
# print(a2.legs)
# print(a3.legs)
# print(Animal.legs)

a2.legs = 2

print(Animal.legs)
print(a2.legs)
print(a3.legs)


# print(Animal.eyes)  GIves Error
a2.eyes = 2
a3.eyes = 4

print(a2.eyes)
print(a3.eyes)



#  -------------------------------
# 1. Instance Method
# 2. Static Method
# 3. Class Method

class Birds():
    eyes = 2
    def __init__(self):
        self.legs = 2
        self.wing = 2

    def fly(self):   # Instance Method
        print("Birds are flying with",self.wing,"wings.")

    @classmethod
    def eat(cls):
        print("This is eat method Under Birds class", cls.eyes)   # Class Method

    @staticmethod
    def buildnest():
        print("Birds build nests using sticks and cotton")
    
b1 = Birds()

b1.fly()   # Birds are flying with 2 wings.
# b1.eat()
# b1.buildnest()   # Birds build nests using sticks and cotton

Birds.buildnest()  # Birds build nests using sticks and cotton
Birds.eat()  # This is eat method Under Birds class 2
b1.fly()   # Gives Error due to Instance Method

