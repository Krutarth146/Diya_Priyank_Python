# from array import *

import array as arr


# Python does not support array but we can use list instead.
# we need import array library.


a = [10 ,20 ,89, 78]
# print(a)

a.append(100)
# print(a)

a.insert(2, 66)
# print(a)

a.pop()   # Removes last element
print(a)

a.pop(2)   # Removes particular Index element
print(a)

a.remove(10)
print(a)    # [20, 89, 78]

# list1 = [4,4,4,4,4,44]
# print(list1)

# for i in list1:
#     print(i)

# import numpy as np
# from numpy import *
# from math import asin


# b = arr.array('i' , [10, 90, 78, 56, 45, 34])

# print(b)   # array('i', [10, 90, 78, 56, 45, 34])
# print(type(b))   # <class 'array.array'>


# for i in b:
#     print(i)
# print(len(b))   # 6

# for i in range(0,6):  # 0 1 2 3 4 5
#     print(b[i],end=" ")


# 
# a = [int(i) for i in input().split()]
# print(a)


floatarray = arr.array('d', [12.90, 90.78, 88])
print(floatarray)

for i in floatarray:
    print(i,end=' ')


floatarray.insert(1,90.88)
print(floatarray)

print(floatarray.pop(2))
print(floatarray)


floatarray[1] = 22
print(floatarray)


list1 = [2, 90, 78, 56, 45]

d = arr.array('i',list1)
print(d)