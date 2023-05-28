# i = 0     # Strat Point

# while i<=100:    # Condition
#     print(i,end='\t')     # Statement
#     i+=2        # Flow i = i + 1


#### Reverse Order
# i = 100

# while i>=1:
#     print(i,end='\t')
#     i-=1


# Prime Number Using Flag

# num = int(input("Enter any Number: "))
# i= 2
# flag = 0
# while i<num:
#     if num % i == 0: 
#         flag = 1
#         break
#     i+=1

# if flag==1:
#     print(f"{num} is Not Prime Number")
# else:
#     print(f"{num} is Prime Number")


# Prime Number using Counter
# num = int(input("Enter any Number: "))
# i= 2
# flag = 0
# while i<num:
#     if num % i == 0: 
#         flag = 1
#         break
#     i+=1

# if flag==1:
#     print(f"{num} is Not Prime Number")
# else:
#     print(f"{num} is Prime Number")






num = int(input("ENter Any Number: "))
sum = 0
mul = 1
# 22 - > 2+2 = 2*2
while num>0:
    rem = num % 10   # rem = 8
    sum = sum + rem  # sum = 22
    mul = mul * rem  
    num = num // 10   # num = 0

if mul == sum:
    print("Twin Number")
else:
    print("Not Twin Number")


# Perfect Number

# 6 -> 2 , 3, 1 -> 2+3+1 = 6 -> Perfect Number

# 8 -> 1, 2, 4 -> 1+2+4 = 7 -> Not Perfect Number
