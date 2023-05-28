
# Sequence

# 1. Strings

# str1 = "Hello Python"
# print(len(str1))

# l = len(str1)
# print("Length of Your string is ",l)


# Indexing

str2 = "Royal_Technosoft_"
str3 = "U2345678_Dhiraj Sir"
# print(str2[0])
# # print(str2[-1])
# print(str2[-3])
# print(str2[5])
# print(str2[0:8])   # 0 is Starting Position and 8 (n-1) is last Position
# print(str2[2:8])   #n-1
# print(str2[5:13])
# print(str3[13:15])
# print(str3[100])  # Gives Error
# print(str3[2:100])
# print(str3[:9])
# print(str3[:])
# print(str3[4:13:3])

print(str3[2::2])
# print(str3[:3:])
# print(str3[::3])
# print(str3[1::])
print(str3[::3496])
##################################################



# print(str1[5])  #1  Ans. _
# print(str1[0])   #2  Ans. H
#print(str1[-1])  #3 Ans. i
# print(str1[1:4])   #4  Ans. ell
# print(str1[4:10])   #5    Ans. o_My n
# print(str1[10:4])  #6   Ans. 
# print(str1[:])    #7       Ans. All Characters of str1
# print(str1[1:])  #8       Ans. ello_My name Is Priyank Modi
# print(str1[:6])   #9      Ans. Hello_
# print(str1[::-1])     #10  Ans. idoM knayirP sI eman yM_olleH
# print(str1[2:7:1])     #11      Ans.    llo_M
# print(str1[1:7:4])    #12     Ans.  e_  
# print(str1[::-1])     #13     Ans. idoM knayirP sI eman yM_olleH

str1 = "Hello_My name Is Priyank Modi"
# print(str1[-9])         #Ans. y
# print(str1[-9:-2])     #14     Ans.  yank Mo  
# print(str1[2:6:-1])       #15       Ans.   
# print(str1[6:2:-1])       #16       Ans. M_ol
# print(str1[2:9:-2])       #17       Ans. 
# print(str1[5:10:-4])      #18       Ans.
# print(str1[1::])      #19       Ans. ello_My name Is Priyank Modi
# print(str1[::-2])     #20       Ans. io nyr Iea MolH
# print(str1[::])       #21   Ans. Hello_My name Is Priyank Modi
# print(str1[:4:])   #22  Ans. Hell
# print(str1[:5:-2])   #23   Ans. io nyr Iea M
# print(str1[1:5:])     #24 Ans. ello
# print(str1[5:1:])     #25  Ans. 
# print(str1[-1])    Ans. i
# print(str1[:-1:])     #26  Ans. Hello_My name Is Priyank Mod 


# Strings Methods
str1 = "royAl_TEchno1234"

# print(str1.upper())   # Convert into capital letters

# print(str1.casefold())  # Convert Into Small letter

# print(str1.capitalize())   # Capitalize only first character

# print(str1.lower())  # Convert into small

# print(str1.center(30,'*'))    # POsition at center and place character
str2 = "Apples Diya////is Honest Girl. Apple"

str3 = "Ståle"

# # print(str2.count("Apples", 0, 10))  # Ans. 1
# # print(str3.encode())   #utf 8 
# print(str3.encode(encoding = "ascii", errors="backslashreplace"))  #  Replace with Backslash
# print(str3.encode(encoding = "ascii", errors="ignore"))     # Ignorte This Chararcter
# print(str3.encode(encoding = "ascii", errors="namereplace"))  # Replace with name
# print(str3.encode(encoding = "ascii", errors="replace"))   # Encode with ?
# print(str3.encode(encoding = "ascii", errors="xmlcharrefreplace"))  # Replace with xml character


txt1 = "Hello\tWelcome my world."
# print(txt1.expandtabs())   # Control Tab size Default 8    
# print(txt1.expandtabs(10))
# print(txt1.expandtabs(25))

# x = txt1.endswith(".", 1 ,26)  # Check the word in the last position of the string and return True or false
# print(x)

# Format Method
# txt4 = "For only {diya: .2f} dollars!"

# print(txt4.format(diya = 49))


# txt4 = "For only {diya} dollars!"

# print(txt4.format(diya = 49))


# txt5 = "I am {name} and I am studying in {std}th Standard.".format(name = "Diya" , std = 9)

# print(txt5)

# txt5 = "I am {0} and I am studying in {1}th Standard.".format("Priyank", 12)
# print(txt5)

txt5 = "I am {4} and I am studying in {1}th Standard.".format("Priyank", 12,100,"Diya","Mohan")
# print(txt5)

# txt5 = "I am {} and I am studying in {}th standard.".format("Diya", 9)
# print(txt5)


# fstring 
# name = "Shakti Mohan"
# print(f"Hey This is {name}")

# a = 12
# b = 32
# c = a+b
# print(f"Sum of a and b is {c}")


# format_map


# a = {'x': 'Diya', 'y': 'Gandhi'}
# str3 = "Hello my First name is {x} and Last name is {y}.".format_map(a)   # Dictionary Type
# print(str3)

# priyank = ()  # Tuple
# print(type(priyank))

# priyank = []   # List
# print(type(priyank))

# priyank = '123'   # string
# print(type(priyank))

# priyank = {}  # Dictionary -> Key : Value
# print(type(priyank))

# priyank = {2,}   #set
# print(type(priyank))

# str4 = "Krutarth345"

# x = str4.index('h', 1, 10)   # Gives Index of Particular Character
# print(x)

# print(len(str4))   # Find Length of string

# y = str4.isalnum()  # Check Alphabetic NUmerical Values and returns True Or false
# print(y)

# y = str4.isalpha() # Check Alphabets Elements & returns True Or false
# print(y)

# print("Kruta\bth") # backspace

# print("Krut\r12345")  # Carriage Return




# x = str5.index('o',2,12)
# print(x)

# print(len(str5))

# y = str5.isalnum()
# print(y)

# y = str5.isalpha()
# print(y)

# print("Kr\butarth")

# print("Krut\r1")   # Ans. 1rut

str5 = "royal technosoft123"
# x = str5.isdecimal()
# print(x)


# x = str5.isascii()
# print(x)

# x = str5.isdigit()
# print(x)

# x= str5.isidentifier()
# print(x)

# x = str5.islower()
# print(x)

# x = str5.isnumeric()
# print(x)

# x = str5.isprintable()
# print(x)

# x = str5.isspace()
# print(x)

# x = str5.istitle()
# print(x)

# x= str5.isupper()
# print(x)

# Joins 

# a = "Priyank"
# myTup = ("Hello " + a + " How are u?")
# print(myTup)

# myTuple = ("Diya", "Gandhi", "Priyank")
# x = '_'.join(myTuple)
# print(x)

# left Justify
# txt11 = "apple****W"

# x = txt11.ljust(10)

# print(x, "is my favourite fruit.")


# # lstrip
# txt = "    banana    "
# x = txt.lstrip()
# print(x + " Hello")


# print("""Introduction: 
# \tName: Diya Gandhi""")

# # Introduction:

# #         Name: Diya Gandhi

# maketrans

# str11 = "wp"

# str22 = "Kr"

# str33 = "dd"

# txt66 = "My name is wputaddrth"

# table = txt66.maketrans(str11,str22,str33)

# print(txt66.translate(table))


# Partition Method

# txt7 = "Diya is Good Good Girl Girl"

# x = txt7.partition("Good")
# print(x)


# txt7 = "Priyank is bad boy"

# x = txt7.replace("bad" , "Good")

# print(x)

# print("Ashok")
# print("Mina")

# rfind Method
txt7 = "Diya is Su\ncasa"
# x = txt7.rfind("Mu")
# print(x)

#rindex()
# x = txt7.rindex("masa")
# print(x)

# rpartition
# x = txt7.rpartition("Su") 
# print(x)

# x = txt7.rstrip()
# print(x + "Hey") 
txt7 = "         Diya is Su casa            "

# splitlines
# x = txt7.splitlines()
# print(x)


# startswith
x = txt7.startswith("D")
print(x)

# x= txt7.strip()
# print(x)

# #swapcase
# x = txt7.swapcase()
# print(x)

# transalate method
# myDict = {83: 82}     # 82 -R, 89 Y

# txt55 = "Hello Sam"
# print(txt55.translate(myDict))

# # zfill()
# txt90 = "30"

# x = txt90.zfill(5)
# print(x)


































