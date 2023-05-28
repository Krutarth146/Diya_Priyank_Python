# list - []                  - Mutable      ordered   Allow Duplicates
# tuple  ()                  - Immutable     ordered   Allow Duplicates
# set    {} or set()         - Unchangeble  Unordered Don't Allow Duplicates
# frozen set {}              - Imutable     Unordered Don't Allow Duplicates
# dict   {} (Key -value Pair)- Mutable      Ordered   Don't Allow Duplicates

# record = {
#     '1001' : {'pName' : "Parle G", 'qn' : 220, 'price' : 5},
#     '1002' : {'pName' : 'Kellogs', 'qn' : 180, 'price' : 50},
#     '1003' : {'pName' : "5 Star", 'qn' : 40, 'price' : 20},
#     '1004' : {'pName' : "Dairy Milk", 'qn' : 140, 'price' : 15}
# }

import json
f1 = open("record.txt","r")
# Json ---> Javascript Object Notation
x = f1.read()
record = json.loads(x)
f1.close()


# print(record)
# print(record['1003']['price'])   # 20
# print(record['1002']['qn'])   # 180
# print(record['1002']['pName']['brand'])   # Adani

# print(len(record))  # 4
# print(record.__sizeof__())  # 216

# print(isinstance(record,dict))   # True

# from sys import getsizeof
# print(getsizeof(record))  # 232

# import bidict

# print(record)


print("--------------------Menu-----------------------")

for i in record:
    print(i,'------', record[i]['pName'], record[i]['qn'],"------>" ,record[i]['price'])

user_need = input("Enter Product Id: ")
quantity = int(input("Enter QUantity: "))

if quantity <= 0:
    print("Pls Enter Valid Quantity.")
    exit()


total_bill = 0
if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print("Your Total Bill AMount is",total_bill)
    print("Thank You! Inventory Updated")
else:
    print(f"We have Only {record[user_need]['qn']} quantity.")
    x = input("If you need then Press y or Y: ")
    if x.lower() == 'y':
        total_bill = record[user_need]['qn'] * record[user_need]['price']
        record[user_need]['qn'] = 0
        print("Your Total Bill Amount is",total_bill)
        print("Thank You! Inventory Updated")


fp = open("record.txt","w")
# Json ---> Javascript Object Notation

import json

js = json.dumps(record)
fp.write(js)
fp.close()


# bill.txt, ---> User Name, Date, Bill Amount
# bill.txt -> bill.csv , Formatting

