# # Operators

# # 1. Arithmetic Operators

# # + , - , * , / , % ,  // , **

# from numpy import bitwise_and


# a = 74
# b = 56

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b) # 74/56 # return float Value Ans. 1.3214285714285714
# # print(a//b)   # return floor Value Ans. 1

# # print(a%b)  # Gives reminder

# # x = 658 
# # reminder = x % 10
# # print(reminder)

# # reminder = x % 100
# # print(reminder)
# a = 3   
# b = 2
# # print(a*b)
# # c = a ** b  # Ans. Power
# # print(c)
# # 2*2*2
# # 4*4*4*4
# # 10*10
# # print(c)
# # print(type(c))

# # Precedence
# # P - Parenthesis
# # E - Expontiation
# # M - Multiplication  # Multiplication and Division Have same Priority.
# # D - Division
# # A - Addition  # Subtraction And Addition have same Priority.
# # S - Subtraction

# # print((3 - 2) * 4)
# # print(6 + 10 * 6 - 9 // 7)  # Ans. 65


# # Comparison Operatotrs

# # < , > , <=, >= , ==, !=
# x, y = 78,78
# # x = 78
# # y = 78

# # print(x < y)
# # print(x > y)
# # print(x <= y)
# # print(x >= y)
# # print(x!=y)
# # print(x==y)
# # print(id(x))
# # print(id(y))
# # print(x is y)    # Return True
# # print(x is not y)    #Return False

# # = is assignment O/p
# # == is Comparison O/p

# # Logical Operators
# # Logical AND, Logical OR, LOgical NOT

# a = False # 0
# b = True  # 1
# # print(a and b)

# # AND 
# #  0  0  | 0
# #  0  1  | 0
# #  1  0  | 0
# #  1  1  | 1


# # print(a or b)

# # OR 
# #  0  0 | 0
# #  0  1 | 1
# #  1  0 | 1
# #  1  1 | 1


# # print(not a) 


# # Bitwise Operators

# # performs Bit by bit Operations and used to operate binary numbers
# # &  |  ~  ^  <<  >>

# # a = 67        #100011        2 | 67   Reminder
#                         #    2 |  33     1
#                         #    2 |  16     1
#                         #    2 |  8      0
#                         #    2 |  4      0
#                         #    2 |  2      0
#                         #      |  1
                    
# # b = 39   #100010
# # print(a >> b)  # 67 >> 2           1 0 0 0 


# # 1 0 1 0
# # 0 1 0 0
# # --------
# # 1 1 1 0


# # print(a | b)
# # print(a & b)
# # 67 << 3
# # print(56 >> 4)                # 11  ->    3
# # 78 << 2
# # print(349 << 3)         # 101011101000 -> 2792
# # print(349 >> 3)            # 101011  -> 43 

# # AND Table (a&b)
# # a  b | O/P

# # 0  0 |  0
# # 0  1 |  0
# # 1  0 |  0
# # 1  1 |  1


# # 1 0 0 0 1 1
# # 1 0 0 0 1 0
# # ------------

# # 1 0 0 0 1 0

# # 2 + 32
# # 34


# # OR table
# # a  b | O/P

# # 0  0 |  0
# # 0  1 |  1
# # 1  0 |  1
# # 1  1 |  1


# # XOR TABLE
# # a  b | O/P

# # 0  0 |  0
# # 0  1 |  1
# # 1  0 |  1
# # 1  1 |  0

# a = 4   
# b = 10   # 100

# c = True
# d = False

# # print(a+b)  # ARithmetic
# # print(not d)   # Logical O/p   printf("%d",(c&&d));
# # print(a & b)     # Bitwie O/p
# e = 66  # 1000000

# # 2 | 64
# # 2    32  0
# # 2    16   0
# # 2    8     0
# # 2    4   0
# # 2    2   0
# # #     1   0
# # print(~ e) # Bitwise Not O/p    # 0111111  # 63

# # print(a ^ b)  # XOR
# # d=4   # 1.00
# # print(d >> 2)

# # Assignment O/p

# # +=, -=, *=, /= %= //= **a 

# # print(25/2)   # FLoat
# # print(25//2)  # Floor
# a = 65
# b = 2

# # a**=b 
# # print(a)

# # a//=b
# # print(a)

# # a&=b
# # print(a)

# a|=b
# print(a)

# a = b   # Assignment O/p
# print(a)

# # a == b  # Comparison O/p

# a^=b
# print(a)

# a>>=b
# print(a)


# a<<=b     a = a >> b
# print(a)
# printf("%d",(a+=b));
# Arithmetic
# bitwise
# Relational
# Logical
# Assignment


# Identity Operator

diya = 10
priyank = 20

# krutarth = diya
# # print(krutarth)
# print(id(diya))
# print(id(krutarth))

# # # print(diya is priyank)
# print(diya is not krutarth)

# Membership O/p
# in and in not

# in    True if value is found in sequence
# not in   True if value is not found in sequence


x = 24
y = 20

list1 = [10, 20, 24 ,30 ,40, 50, 'Diya', 34.5, True]

# if(condition)
# {
#                     printf("csdhcbdvh");

# }else{


# }


# if (x not in list1):
#     print("x is present in list1")
# else:
#     print("x is not present in list1")


# Precedense and assoiciativity

# expr = 10 + 20 * 30
# print(expr)

# expr = (10 + 20) * 30
# # print(expr)

# name = "Alex"
# age = 0

# if name=="Alex" or name == "Priyank" or age <=2:
#     print("Welcome")
# else:
#     print("Goodbye")

# print(5-(2+3))

# print(2 ** 3 ** 2)   # Right to Left

# [on_true] if [expression] else [on_false]


a, b = 20, 10

# min = a if a < b else b
# print(min)

# if a != b:
#     if a>b:
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# else:
#     print("a equals to b")



# print("Both are equal" if a==b else "a is greater than b" if a>b else "b is greater than a")

# print("a is greater than b" if a>b else "b is greater than a")

# print("The Min amount from a and b")
# max = b if a<b else a
# print(max)

# Bitwise Not Operator

x = 60  # 60 - 111100 (Binary number)
y = ~x  #      000011 (Negation)   ->  Finding 2's Complement Ans. (111101)  ->  Decimal (61)
print(y) #   Ans. -61

p = -90
print(~p)  # Ans. 89

# Task: WAP to check leap year or Not.

'''
2's Complement

0       1       1
1       0       1
__      __      __
1       1       10 (1 as carry)
'''