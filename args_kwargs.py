# Functions --------


# 1. takes Nothing and return nothing
# 2. takes Something and return nothing
# 3. takes Nothing and return Something
# 4. Takes Something and Return Something



# Premitive
# print()
# input()


# User Defined 

#  1. takes Nothing and return nothing
def priyank():
    print("This is Priyank Method")

priyank()  # This is Priyank Method


# 2. takes Something and return nothing

def Diya(x,y,z):
    print(40+50+60)

Diya(40,50,60)   # 150


# 3. takes Nothing and return Something

def krutarth():
    return 90 + 80

print(krutarth())   # 170


# 4. Takes Something and Return Something

def royal(name, marks):
    return(name,marks)


print(royal("Krutarth Patel", 90.89))  # ('Krutarth Patel', 90.89)


def add(num1, num2 ,num3=0):
    return num1 + num2 + num3


print(add(10,20))   # 30


def pri_name(name1, name2, name3=None):
    return(name1, name2, name3)

x = pri_name("Priyank", 'DIya', 'ROyal')
print(x)

t = None
print(type(t))  # <class 'NoneType'>


m = True
w = 20

print(m+w)   # 21   # Implicit TYpecasting


g = 90
f = float("56")
print(g+f)   # 146.0  # Explicit Typecasting



def func1(std, *www):    # args
    # print(args)
    for _ in www:
        print(_,end=' ')

func1(90,32,23,3,3,4,5, "Priyank", "DIya")
print()

# Program -> Calculate of arguments and print sum and average


# kwargs   -> DIctionary


def Intro(**kwargs):
    for priyank in kwargs.items():
        print(priyank)

Intro(name = "Krutarth", salary = 10, address = "Karnavati")

# Ans.
# ('name', 'Krutarth')
# ('salary', 10)
# ('address', 'Karnavati')