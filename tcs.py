# TW =130 FW=70

# 200  -> Value of V
# 540   -> Value of W

x = ((200*4) - 540) // 2
print(x)
print(200 - 130)

# --------2  ---------------------

str1 = "**##*#*##Hello#"
list1 = []
for i in str1:
    list1.append(i)

print(list1)

dict1 = {}
for i in list1:
    if i == '#' or i=='*':
        dict1[i] = list1.count(i)
print(dict1)
    
if dict1['*'] == dict1['#']:
    print(0)
elif dict1['#'] > dict1['*']:
    print(-1)
elif dict1['#'] < dict1['*']:
    print(1)
