'''
list

List is a collection which is ordered and changeble.   Allows Duplicate Members.

Change the value of the list   --> mutable/Changeble

syntax:

'''

mylist = []

print(type(mylist)) # <class 'list'>

chars = ['a','b','h','g']
numbers = [1,2,3,4,5,6,7,9999]
names = ['Diya','Priyank','Steve','Krutarth']
mix_list = ['a', 234, 'b', 'bob', 'apple', 8888]   # Ordered


# print(chars)
# print(numbers)
# print(names)
# print(mix_list)

veg = ['tomoto', 'potato', 'cucumber', 'carrot', 'onion']

# print(veg[-1])   # cucumber
# print(veg[4])    # cucumber
# print(veg[0])    # totmato
# print(veg[2])    # print(veg[-3])   # Carrot

print(max(veg))   # tomoto
print(min(veg))   # carrot
print(len(veg))   # 5

list2 = veg   # list2 is a reference to veg

# print(list2)   # list2 is just a label to veg


veg.append('cabbage')
print(veg)   # ['tomoto', 'potato', 'cucumber', 'carrot', 'onion', 'cabbage']
print(len(veg))  # 6

list3 = [34, 89, 78 , 'a', 'dvdavadv']
print(len(list3))  # 5

veg.append(list3)   # add a New item to the list
print(veg)

list4 = [56,89]
veg.extend(list4)
print(veg)

veg.extend('Berry')
print(veg)

# veg.clear()  # Clear the List

veg.append('berry1')
veg.append('berry1')
print(veg)

print(veg.count('berry1'))   # Ans. 2  # Count the Number of similar items in the list



print(veg.index('carrot'))  # Find the index of the item

veg.reverse()  # Reverse the List
print(veg)
veg.append('grapes')
list3 = veg  # list3 is a reference to veg
print(list3)

list4 = veg.copy()  # Returns a shallow copy of the list
# veg.append('Yesha')
print(list4)


veg.remove('berry1')
veg.remove('berry1')
veg.remove('carrot')   # Remove the item from the list
print(veg)


veg.append('Priyank')
print(veg)

veg.insert(2, 'Diya')   # insert the item at the specified Index
print(veg)

veg[3] = 789  # Replace the item at the specified index
print(veg)


# Task : Make a one fruit list then take input from the user and check whether that fruit is in the list or not??