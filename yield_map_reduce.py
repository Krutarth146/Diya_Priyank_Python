def priyank(num):
    for w in range(num):
        # print(w)
        yield w



num1 = 20
for t in priyank(num1):
    print(t)  # 0


# 22 -> 2+2 , 2*2  = 4 (Perfect Number)


num = int(input())

def perfect(num):
    sum = 0
    mul = 1
                                                                                                            

    while num > 0:
        rem = num % 10    # 2
        sum = sum + rem
        mul = mul * rem
        num = num // 10

    print(sum)
    print(mul)
    if sum == mul:
        return 1
    

if perfect(num) == 1:
    print("Perfect")