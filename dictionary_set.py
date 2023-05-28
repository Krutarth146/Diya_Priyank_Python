dict1 = {
    "Name" : "Priyank",
    "Roll" : 900,
    "year" : 2004,
    "year" : 2005
}

# Dictionaries: Ordered, Changeble, Do not allow Duplicates

print(dict1["Name"])   # Priyank
print(dict1["year"])   # 2005
print(dict1)   # {'Name': 'Priyank', 'Roll': 900, 'year': 2005}
print(type(dict1))   # <class 'dict'>

print(len(dict1))   # 3                                           

dict2 = {
    "Name" : "Diya",
    "roll" : 400,
    "Active" : True,
    "hobby" : ['cricket', 'cooking']
}
print(dict2)  # {'Name': 'Diya', 'roll': 400, 'Active': True, 'hobby': ['cricket', 'cooking']}

# We can also create dictionary using dict() constructor

dict3 = dict(name = "Ashok", age = 80, country = 'India')

print(dict3)  # {'name': 'Ashok', 'age': 80, 'country': 'India'}


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members

print(dict3['name'])

x = dict3.get('age')
print(x)  # 80

y = dict2.keys()
print(y)   # dict_keys(['Name', 'roll', 'Active', 'hobby'])

h = dict2.keys()
print(h)

dict2["color"] = "Yellow"
print(h)   # dict_keys(['Name', 'roll', 'Active', 'hobby', 'color'])


g = dict2.values()
print(g)   # dict_values(['Diya', 400, True, ['cricket', 'cooking'], 'Yellow'])

f = dict2.items()
print(f)   # dict_items([('Name', 'Diya'), ('roll', 400), ('Active', True), ('hobby', ['cricket', 'cooking']), ('color', 'Yellow')])

dict2["color"] = "red"
print(f)   # dict_items([('Name', 'Diya'), ('roll', 400), ('Active', True), ('hobby', ['cricket', 'cooking']), ('color', 'red')])

if "roll" in dict2:
    print("Roll is available in dict2")

dict2.update({"roll" : 500})
print(f)   # dict_items([('Name', 'Diya'), ('roll', 500), ('Active', True), ('hobby', ['cricket', 'cooking']), ('color', 'red')])

dict2["roll"] = 100
print(f)

dict2.pop("roll")
print(dict2)   # {'Name': 'Diya', 'Active': True, 'hobby': ['cricket', 'cooking'], 'color': 'red'}

dict2.popitem()
print(dict2)   # {'Name': 'Diya', 'Active': True, 'hobby': ['cricket', 'cooking']}

del dict2['Name']
print(dict2)   # {'Active': True, 'hobby': ['cricket', 'cooking']}

# del dict3
# print(dict3)

# dict1.clear()
# print(dict1)   # {}

dict2['Active'] = None
print(dict2)

# Using Loops

for c in dict2:
    print(c)

for v in dict2:
    print(dict2[v])

for t in dict2.values():
    print(t)

for j in dict2.keys():
    print(j)

for q,i in dict2.items():
    print(i)


# Nested Dictionaries

myFamily = {
    "child1" : {
        'name' : 'Priyank',
        'year' : 2003
    },
    "child2" : {
        'name' : 'Diya',
        'year' : 2003
    },
    "child3" : {
        'name' : 'Manoj',
        'year' : 2003
    }
}

print(myFamily)  # {'child1': {'name': 'Priyank', 'year': 2003}, 'child2': {'name': 'Diya', 'year': 2003}, 'child3': {'name': 'Manoj', 'year': 2003}}

child1  =  {
        'name' : 'Priyank',
        'year' : 2003
    }

child2 = {
        'name' : 'Diya',
        'year' : 2003
    }

child3 = {
        'name' : 'Manoj',
        'year' : 2003
    }

dict3 = {
    child1,

}