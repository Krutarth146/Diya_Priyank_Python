def sum():   # Func. defination
    print(10+20)

sum()   # func. calling   # 30

# lambda -> (Anonymous Function)

myFunc = lambda x : x + 10

x = myFunc(90)   # print(myFunc(90))
print(x)

cube = lambda x:x*x*x
print(cube(8))   # 512



# help(authors.sort())
# print(authors)

# authors.sort(key=None,reverse=False)
# print(authors)   # ['priyank', 'newton', 'manoj_pandey', 'diya_Gandhi', 'dhiraj_sir']

authors = ['neWton', 'Priyank', 'dHiraJ sir', 'diya Gandhi', 'manoj paNdey']
# authors.sort()
# print(authors)

# for i in authors:
#     print(i.split(',')[-1].lower())

authors.sort(key = lambda name:name.split(',')[-1].upper())
print(authors)


# Quadratic function


def quadratic_fun(a,b,c):
    """Docstring Returns the function f(x) = ax^2 + bx + c"""
    
    return lambda x: a*x**2 + b*x + c

# print(quadratic_fun.__doc__)   # Docstring Returns the function f(x) = ax^2 + bx + c

# f = quadratic_fun(10,20,30)

# print(f(0))  # 30
# print(f(1))  # 10 + 20 + 30 = 60

print(quadratic_fun(1,2,3)(10))  # 100 + 20 + 3 = 123


# H.w

# 1. Create a file in write Mode and write 5 statements in it. then read these statements and print into terminal then find No. of lines , no. of words, No. of charcaters, also find count which word starts with 'D'.


# 2. Lambda 10 programs

# 3. Map, reduce, filter revise it.



# 2 + 22 + 222 + 2222 + 22222 = 24690

num = 2

j=10

# 2 -> 22

# num =  (num % j) * 10 + 2    # 22
j*=10

# num = (22 % j) * 10 + 2    # 222

# num =  (222 % j) * 10 + 2   # 2222

# -> sum = sum + num  # sum = 2 + 22 + 222 + 2222


list1 = [23, 78, 0, 90, 0, 50, 0, 0, 23, 91]
list2 = []
for i in list1:
    if i % 10 == 0:
        list2.append(i)

print(list2)  # [0, 90, 0, 50, 0, 0]


for i in list2:
    if i in list1:
        list1.remove(i)

print(list1)  # [23, 78, 23, 91]

list1.extend(list2)
print(list1)


fp = open("Diya.txt",'w')
fp.write("Hello Diya\nGood AfterNoon.")
fp.close()

fp = open("diya.txt",'r')
x = fp.readlines()

print(fp.tell())  # 27
fp.seek(0)
# for i in fp:
#     print(i)
print(len(x))
fp.close()

from bidict import bidict
ele = {'Name' : "Manoj"}
ele = bidict(ele)

print(ele['Name'])
print(ele.inverse['Manoj'])