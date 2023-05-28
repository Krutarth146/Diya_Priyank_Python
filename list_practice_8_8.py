num = int(input("Enter Any Number: "))
# 178
# find the sum of odd digit
rem = 0
sum = 0
temp = num

while( num>0 ):
    rem = num % 10
    sum = sum + (rem*rem*rem)
    num = num // 10

print(sum)
if temp==sum:
    print(temp,"is Armstrong Number")
else:
    print(temp,"is Not Armstrong Number")