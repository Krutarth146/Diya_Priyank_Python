def palindrome(num):
    rev = 0
    diya = num
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    if diya == rev:
        return 1
    else:
        return 0

num = int(input())
x = palindrome(num)

if x==1:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")


# Task : Check whether the given 4 digit Number is armstrong Number or not using Function. (with Args. and with Return Type.) # 8208