tup1 = (1,8,9,7,6,3)
tup2 = (2, 9, 6, 5, 4,2)
# result = []
# for i in tup1:  # 1, 8, 9 
#     for j in tup2:    # 2,9,6,5,4,2
#         x = [i , j]
#         result.append(tuple(x))

# print(result)


# result = [(i,j) for i in tup1 for j in tup2]
# print(result)



list1 = [(1,9), (67, 10), (12, 34), (2,2), (44,8)]


for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i][1] > list1[j][1]):
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)