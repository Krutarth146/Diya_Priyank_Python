from numpy import true_divide


list1 = [10,10,101,10]   # Allows Duplicates, Indexed, mutable(changeble)
print(list1)

tuple1 = (10,10,101,10)  # Allows Duplicates, Indexed, Immutable(Not Changeble)
print(tuple1)

print(list1.__sizeof__())    # 72
print(tuple1.__sizeof__())   # 56

set1 = {10,10,101,10,80,90}   # Don't allow Duplicates, unIndexed(don't follow Index), mutable(changeble)
print(set1)    # {80, 10, 101, 90}

set2 = {10, 90, 89,78,67}
print(set1.difference(set2))
# print(set1)   # {80, 101}


set3 = {10, 90, 87, 54 ,22 ,20}
set1.intersection_update(set3)
print(set1)   # {10, 90}


dict1 = {80:'Eighty', 90:"Nighty", 70:"Nighty",20:'www'}    # Don't allows Duplicates(Needs Unique keys), Indexed, mutable(changeble)
print(dict1)   # {80: 'Eighty', 90: 'Nighty'}

dict1.update({60:'Sixty'})
print(dict1)


#####################
# fruits = ['mango', 'apple', 'banana', 'lichi']

# user_fr = input("ENter fruit Name: ")

# if user_fr in fruits:
#     print(f"{user_fr} is available.")
# else:
#     print(f"{user_fr} is not available.")

############
# Sum of odd Numbers b/w 1 to 100
# sum = 0
# for i in range(1,101):
#     if i%2!=0:
#         sum += i


# sum = 0
# for i in range(1,101,2):
#     sum += i

# print("Sum of odd Numbers: ",sum)   # 2500

# 1. Mcq
_ = '1 2 3 4 5 6'
print(_)

# 2. Mcq
x = 'abcd'
for i in range(len(x)):
    print(i)    # 0 1 2 3

# What will be Output for this code?
# print(len(x)) # 4


# for i in range(4):
#     print(i) # 0 1 2 3

# for i in range(1, 9):  
#     print(i)  # 1 2 3 4 5 6 7 8

# for i in range(2, 7, 2):
#     print(i)   # 2 4 6


# 3. Mcq
# What happens when '2' == 2 is executed?

# False

# print(type('2'))  # str
# print(type(2))    # int

# if '2'==2:
#     print('True')
# else:
#     print('False')

# 4. Mcq

# {5, 9, 8} # set
# {5: 98} # dictionary


# 5. Mcq
# Who developed the Python language?

# Guido van Rossum

# 6. Mcq
# What do we use to define a block of code in Python language?
# Indetation


# 7. Which of the following operators is the correct option for power(ab)?
# print(a**b)

# 8. Mcq
z = "xyz"
j = "j"

while j in z:
    print(j,end=" ")

# No Output

# 9. Mcq

print()    # built in func.

# 10. mcq
# print('It\'s ok, don\'t worry')    # It's ok, don't worry


# 11. mcq

# Suppose list1 is [2445,133,12454,123], what is max(list1)?
# 12454


# 12 Mcq
# Which one of these is floor division?
# ANs. //
print(22 / 3)  # Returns float  7.333333333
print(22 // 3)   # Returns floor 7 (Integer)


# 13. mcq

# Which of these about a set is not true?
# Mutable data type
# Not allows duplicate values
# Data type with unordered values
# Immutable data type  (Answer)


# 14. mcq
# Which of the following statements create a dictionary?

# d = {}
# d = {“john”:40, “peter”:45}
# d = {40:”john”, 45:”peter”}
# All of the mentioned  (Answer)


# 15. mcq
# Which of these in not a core data type?

# List
# Dictionary
# Set
# Class  (Answer)


# 16. mcq

# i=1:

# while True:
#     if i%3 == 0:
#         break
#     print(i)

# Invalid Syntax


# Which of the following declarations is incorrect?

# _x = 2
# __x = 3
# __xyz__ = 5
# None of these  (Answer)

# True


# What is the default step value of the function range()?

# for i in range(1, 8, 1):
#     print(i)   # 1 2 3 4 5 6 7



# mcq

x = 'pqrs'
for i in range(len(x)):
    x[i].upper()
print (x)   # pqrs


# PQRS
# pqrs
# qrs
# None of these


# mcq
# control statements: 3 (break, pass, continue)

if 1!=1:
    pass
else:
    print("Else block executed")


print(22 % 3)  # 1 reminder



# mcq
# Which of the following is not a keyword in Python language?

# val  (Answer)
# True
# in
# if



