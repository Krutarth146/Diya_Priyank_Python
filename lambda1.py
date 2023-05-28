# Map, Reduce, Filter


list1 = [10,20,30,40,50,60]


ans = list(map(lambda x : x*x, list1))
print(ans)  # [100, 400, 900, 1600, 2500, 3600]

ans1 = list(map(lambda t : t > 10,list1))
print(ans1)  # [20, 30, 40, 50, 60]   # [False, True, True, True, True, True]

import functools

print(functools.reduce(lambda a,b : a+b, list1))   # 210

import itertools

print(list(itertools.accumulate(list1, lambda a,b : a+b)))   # [10, 30, 60, 100, 150, 210] 



import operator

print(functools.reduce(operator.add, ["Krutarth", "Patel"]))   # 210


# Quadratic Funtion


def Quadratic_Funtion(a,b,c):
    return lambda x : (a*x*x) + (b*x) + c



res = Quadratic_Funtion(10,20,30)

print(res(25))  # 6780

# Map, reduce, filter, lambda Ex refer


# -----------------------------------------

def authenticate(email,password):
    if password.isalpha() == False:
        print("Credentials Not Valid")
        return
    
    if email.lower().endswith("@gmail.com"):
        print("Valid Format")
      
    
    if (email.lower() == "admin1@gmail.com" and password == "admin"):
        print("Correct Credentials")
    else:
        print("Wrong Credentials")

email = "admin1@gmail.com"
password1 = 'admin'
authenticate(email,password1)

# 1.
# jony jony yes papa

# JonY JonY YeS PapA


# 2.
# Palindrome   ->  Nayan -> Nayan