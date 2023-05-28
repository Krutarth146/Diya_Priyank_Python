'''
list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
'''

# price = price - (price * 10)/100 

#  3. add 10 numbers into the list, sort that list and print the list
'''
list1 = []

for i in range(10):
    list1.append(int(input("Enter Any Number: ")))

list1.sort(reverse=False)  # Default ASC
list1.sort(reverse=True)  # DESC
print(list1)
'''


#  4. add 10 numbers into the list, remove the duplicates and print the list
    
# l1 = []

# for i in range(4):
#     l1.append(int(input("ENter any Number: ")))

# print(l1)

# # Method - 1

# l2 = []

# for i in l1:
#     if i not in l2:   # Membership O/p
#         l2.append(i)

# print(l2)


# Method = 2

# list1 = [45, 78, 22, 78, 90, 11, 11]
# print(list1)

# list2 = set(list1)
# list2 = list(list2)
# print(list2)


# 5. add 10 numbers into the list, print the maximum and minimum number from the list

l3 = [45, 78, 66, 78, 99, 34, 11]

# print(max(l3))
# print(min(l3))

l3.sort()
print(l3)

print("Maximum Number is",(l3[-1]))
print("Minimum Number is",(l3[0]))


# 6. 6. add 10 numbers into the list, print the average of the list

l1 = []
for i in range(5):
    l1.append(int(input("ENter Any Number: ")))

sum = 0
count = 0
for i in l1:
    sum = sum + i
    count+=1  # Method 1

print("Sum of this NUmbers is",sum)
print("Average of this :",(sum//len(l1))) # Method - 2


# import statisticst

# x = statistics.mean(l1)
# print(x)