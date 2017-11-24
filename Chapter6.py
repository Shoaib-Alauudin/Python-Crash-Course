print("----------------------Chapter-6--(2/April/17)-----------------------")
# print("----------------Dictionary-------------")
# it is also known as JSON format representation
# Student = {"Name":"Shoaib","Age":23,"Roll_No":1074,'c':"Hello Python",1:"Hello World"}
# print(Student["Age"])
# print(Student["Roll_No"])
# print(Student["Name"])
# print(Student['c'])
# print(Student[1])
# Student["Age"] = 22
# print(Student)
# Student["Ali"] = 25
# print(Student)
# del Student["Ali"]
# print(Student)
#
# for keys,values in Student.items():
#     print("Keys: ",keys)
#     print("Values: ",values)
#
# for keys in Student.keys():
#     print("Keys: ",keys)
#
# for values in Student.values():
#     print("Values: ",values)
#

# Set of Dictionary
"""
data = {"Name":"Shoaib",
        "Age":"23",
        "age":"23",
        "Roll_no":"1074"
        }
for A,B in data.items():
    print("A: "+A)
    print("B: "+B)

print("---------Sets---------")

for keys,values in set(data.items()):
    print(keys,values)
"""

# Set of List
"""
names = ['shoaib','Bilal','Zabi','Kamran','Noman']
print(names)
print(set(names))
print("------------------------")
for value in set(names):
    print(value)

print("------------------------")

names = {'name_1':'shoaib',
         'name_2':'Bilal',
         'name_3':'Zabi',
         'name_4':'Kamran',
         'name_5':'Noman'
         }
for name_list,name in set(names.items()):
    print(name_list," : ",name)
"""
# Dictionary of lists
"""
print("-----New------")
Student_Record = {"Names":["Shoaib","Ali","Khan",10,"Muneeb","Munawar","Hadi"],
                  "Age":[10,20,40,50,60,70,80]}
for keys,values in Student_Record.items():
    if 'Shoaib' in values:
        print("We got him")
"""

"""
# print("----------Aliens--------------")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien = [alien_0,alien_1,alien_2]
for value in alien:
    print(value)
print("-------------------------")
# for alie in aliens:
#     for key,value in alie.items():
#         print(key," : ",value)
alien_3 = ('name','age',13,'email',3.142)
alien.append(alien_3)
for value in alien:
    print(value)

print(alien[2],"\n")
print(alien[0]['points'])

"""

#Creating Dictionary
"""
aliens = {}
for alien_number in range(0,30):
    aliens[alien_number]="Hello World"
print(aliens)
"""

# Type casting
"""

print("----------Tuples------------")
first_tuple = (1,2,3,4)
print(first_tuple)
New_list = list(first_tuple)
New_list.append(20)
first_tuple = tuple (New_list)
print(first_tuple)


new_names = ('shoaib','Bilal','Zabi','khan','Muhammad')
print(new_names)
names = list(new_names)
print(names)
names.append('Noman')
names.append('Mehmood')
print(names)
new_names = tuple(names)
print(new_names)

"""
"""
print("A Dictionary in a Dictionary")
users = {
    "UserName":{"Name":"Shoaib","Age":23,"Roll_no":1074},
    "UserName_1":{"Name":"Bilal","Age":23,"Roll_no":1075},
         }

for key,value in users.items():
    print(key," : ",value)
    if 'Shoaib' in value.values():
        print("Shoaib is in a list",' : ',key)
    if 'Bilal' in value.values():
        print("Bilal in a list"," : ",key)
    if 'Name' in value.keys():
        print("Name in a list",' : ',key)

"""

# Lab Tasks
"""
print("---------task-1---------")
value = 1
for values in range(1,10):
    value*=values
print(value)

i=1
value = 1
while i<=10:
    value *= i
    i+=1
print(value)


print("---------task-2---------")
i = 1
value = 0
while i<=100:
    value+=i
    i+=1
print(value)


value = 0
for values in range(1,101):
    value+=values
print(value)
"""

"""
# creating list in a single line
num = list(range(1,11))
num_1 = [value for value in range(1,6)]
num_2 = list(range(0,16))
for value in num,num_1,num_2:
    print(value)

"""

# X = input("Please Enter set of numbers")
# x = X.split(",")
# print(x)
# answer = 0
# i = 0
# while i<=10:
#     answer+=x[i]
# print(answer)
# users = []
# while True:
#     if users == 'exit':
#         print("Thanks for exit")
#         break
#     else:
#         users = input("Please Enter name of users :")
#
# print(users)

# page no: 147
Aliens = []
for new_alien in range(10):
    alien = {"color":"Orange","point":10,"speed":"fast"}
    Aliens.append(alien)
counter = 0
for Alien in Aliens:
    counter +=1
    print(Alien)
print("counter : ",counter)

for Alien in Aliens[:3]:
    if Alien['point'] == 10:
        Alien["color"] = "Green"
        Alien["point"] = 15
        Alien["speed"] = "medium"
for alien in Aliens:
    for value in alien:
        print(value)


