list1 = [10,20,90,80,70,60, 55, 21 ,44, 33]

for i in list1:
    if i % 2 == 0:
        print(i)

# list2 = [i for i in list1]
# print(list2)    # [10, 20, 90, 80, 70, 60, 55, 21, 44, 33]


list2 = [i for i in list1 if i % 5 == 0 or i % 7 == 0]
print(list2)    # [70]


# num = int(input("ENter Frequency: "))

# list1 = []
# for x in range(num):
#     diya = int(input())
#     list1.append(diya)

# print(list1)   # [10, 75, 34, 76]


# list3 = [int(s) for s in input().split('_')]
# print(list3)   # [23, 56, 11, 44, 22, 88, 36]

# Tuple Comprehension


# Method 1
tup1 = (100, 90,89,12,12,45,90)
tup2 = (25, 78,56,43,22,12,55)
# result = []
# for i in range(len(tup1)):
#     mod = tup1[i] % tup2[i]
#     result.append(mod)

# result = tuple(result)
# print(result)


# # Method - 2
# tup3 = (i%j for i, j in zip(tup1,tup2))
# # print(tup3)  # <generator object <genexpr> at 0x000002DD1A2C9A10>

# print(tuple(tup3))   # (0, 12, 33, 12, 12, 9, 35)


# Method - 3
from operator import mod
tup4 = tuple(map(mod, tup1, tup2))
print(tup4)   # (0, 12, 33, 12, 12, 9, 35)
 



# # -------------------------------------------------------------------
# list1= [x for x in enumerate(tup1)]
# print(list1)   # [(0, 100), (1, 90), (2, 89), (3, 12), (4, 12), (5, 45), (6, 90)]


