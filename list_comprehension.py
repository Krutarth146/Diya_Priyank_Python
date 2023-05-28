# list1 = [10, 90, 79, 67, 45, 23]

# list2 = [y for y in list1 if y % 2 != 0]
# print(list2)   # [79, 67, 45, 23]


# Eval Function

# print(3+2)

# x = input("ENter One Number: ")
# y = input("ENter One Number: ")
# print(eval(x) + eval(y))

# print(eval(input("ENter any Expression: ")))   # 72

# x = compile("2**4", "<string>", "eval")
# print(x)   # <code object <module> at 0x0000017C4BD57730, file "<string>", line 1>
# print(eval(x))   # 16


x = 10
y = 40
y = eval("x+y+10-23",{"x":x, "y":y})
print(y)   # 37


# --------------------------------


# list1 = [[13,83,62],
#          [23,45,67],
#          [67,89,45]]

# print(list1)  # [[13, 83, 62], [23, 45, 67], [67, 89, 45]]

# for x in list1:
#     for h in x:
#         print(h,end=' ')

#     print()

main = []

dim = int(input())


for i in range(dim):
    list1 = [int(i) for i in input().split()]
    main.append(list1)

# print(main)

for row in range(len(main)):
    if row % 2 == 0:
        for h in range(len(main[0])):
            print(main[row][h],end=' ')
    elif row % 2 != 0:
        for h in range(len(main[0])-1,-1,-1):
            print(main[row][h],end=' ')


