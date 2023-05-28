# Functions -> Code Reusability

# 1. without Return Type and without Arguments
# 2. without Return Type and with Arguments
# 3. with Return Type and without Arguments
# 4. with Return Type and with Arguments


# 1. without Return Type and without Arguments

def sum():
    a = 10
    b = 90
    print(a+b)

def div():
    a = 10
    b = 90
    print(a//b)

sum()    # Func. Calling   # 100
div()    # 0

# 2. without Return Type and with Arguments

def mul(a,b,c):
    print(a*b*c)

mul(90,1,2)


# 3. with Return Type and without Arguments

def power():
    a = 10
    b = 2
    return a**b

print(power())   # 100


# 4. with Return Type and with Arguments

def sub(a,b,c):
    return a-b-c


print(sub(90, 60 ,20))   # 10