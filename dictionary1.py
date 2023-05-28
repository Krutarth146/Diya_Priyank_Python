# dict1 = {"list1" : [1,3,4,5,6,7,23,445], 
#             "list2" : [5,6,7,4,5], 
#             "list3" : [56,2,2,3,3,3,3]}
# list5 = []
# for i in dict1.values():   # [1,3,4,5,6,7,23,445]
#     # print(i)
#     for j in i:
#         if j not in list5:
#             list5.append(j)

# print(list5)   # [1, 3, 4, 5, 6, 7, 23, 445, 56, 2]


dict2 = {"name" : "Krutarth", "ROll" : 564, "age" : 90}

list8 = ["name"]

for j in dict2:
        if list8[0]==j:
            print("Id is found")
            dict2.pop(j)
            break

print(dict2)   #  {'ROll': 564, 'age': 90}