# Files

# Modes

# "w" - (write mode) IF file is not present then it will create a new file , If already exists then it will write in this file. 'w' mode over-write the file content.
# 
# "r" - (Read Mode) If file does not exists then it will raise an error 

# "a" - (Append Mode) Required file. Data will written after the last line of existing file.

# "x" - IF file is not present then it will create a new file

# 't' - (Text Mode) It will open file in Text Mode

# 'b' - (Binary Mode)  It will open file in Binary Mode

# '+' - In this we can perform Read and write operation together.


# fp = open("Priyank.txt","w")

# fp.write("Hello This is Diya!")

# fp.close()

# fp = open("Priyank.txt", 'r')

# x = fp.read(300)
# print(x)
# print(fp.tell())   # 0
# print(fp.readline())  # Hello This is Diya!
# print(fp.tell())   # 21
# print(fp.readline())  # Royal is Best
# print(fp.tell())   # 37

# print(fp.readlines())   # ['Hello This is Diya!\n', 'Royal is Best \n', 'India is also Best Country.\n', 'Priyank Modi  - Surat']
# print(fp.tell())

# fp.seek(14)
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())

# x = fp.read(300)

# for i in x:
#     print(i, end='')
# fp.close()


# ----------------------------------------------

# f = open("diya1.txt",'a+')


# f.write("Hello")
# f.writelines("Hello This is Priyank Modi\n He is studying in Royal since 1996")

# print(f.tell())

# f.seek(0)
# print(f.readlines())  # ['HelloHello This is Priyank Modi\n', ' He is studying in Royal since 1996HelloHello This is Priyank Modi\n', ' He is studying in Royal since 1996HelloHello This is Priyank Modi\n', ' He is studying in Royal since 1996HelloHello This is Priyank Modi\n', ' He is studying in Royal since 1996HelloHello This is Priyank Modi\n', ' He is studying in Royal since 1996']

# f.close()

# f1 = open("mountain.jpg",'rb')

# f1.read()


# f2 = open("m1.jpg",'wb')

# for x in f1:
#     f2.write(x)


import pickle
filename = 'pm1.txt'
f = open(filename,'wb')

list1 = ['mango', 'banana', 'orange', 'grapes', 'lichi']
list2 = ['mango', 'banana', 'lichi', 'orange', 'grapes']
pickle.dump(list1, f)
pickle.dump(list2, f)

f.close()

f = open(filename,'rb')

x = pickle.load(f)
y = pickle.load(f)
# list1 = []
# list1 = pickle.loads(f)
print(x,y)   # ['mango', 'banana', 'orange', 'grapes', 'lichi']
# print(type(x))   # <class 'list'>
# print(z)

# 1. Read one Text file
# 2. write yourself to one xtext file and then read these text