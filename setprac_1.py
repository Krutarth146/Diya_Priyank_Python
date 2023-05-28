set1 = {90,889,22,3,4}
set2 = {90,889}

print(set1.isdisjoint(set2))   # False if element common in both sets.
print(set2.issubset(set1))   # True
print(set1.issuperset(set2))

tup1 = (90, 78, 67 ,23, 23)
tup1 = frozenset(tup1)
print(tup1)  # frozenset({90, 67, 78, 23})

list1 = [10,20,30,40]
list1 = frozenset(list1)
print(list1)  # frozenset({40, 10, 20, 30})

# print(list1[3])  # Immutable set
print(type(list1))  # <class 'frozenset'>

# Frozenset - It is Method which creates Immutable set object from an iterable.




set1 = {10,20,30,40,50,60}
set2 = {51,61,22,33,3,4}

print(set2.issubset(set1))   # True
print(set1.issuperset(set2))   # True
print(set1.isdisjoint(set2))   # True


dict1 = {
    'list1' : [10,20,30,40,50],
    'list2' : [4,5,6,7,8,2],
    'list3' : [32,4,5,6,40,50,60],
    'list4' : [1,2,3,4,7,8,2]
}

list3 = []
for i in dict1.values():
    for k in i:
        list3.append(k)

print(list3)


str1 =  "MISSISSIPPI"

list1 = [i for i in str1]
print(list1)

dict1 = {}  # {'M': 1, 'I': 4, 'S': 4, 'P': 2}

for j in list1:
    if j in dict1:
        dict1[j] += 1
    else:
        dict1[j] = 1
print(dict1)

dict2 = {}
for h in list1:
    counter = list1.count(h) 
    dict2[h] = counter
print(dict2)  # {'M': 1, 'I': 4, 'S': 4, 'P': 2}


dict1 = {2:34, 90:67}

for i,j in dict1.items():
    print(i+j)