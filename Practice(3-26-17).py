import this # Some lines of sentences
'''
name  = input("Please Enter your Name")
print(name)
message = "Hello Python"
print(message)
NewMessage = "New Hello World Pyhton"
print(NewMessage)
'''

Name = " shoaib alauddin "
print(Name.title()+" Title Case")
print(Name.upper()+" Upper Case")
print(Name.lower()+" Lower Case")
print("Hello World"+Name)           # Split
print("Hello World"+Name.lstrip()) #  Left Split
print("Hello World"+Name.rstrip()) #  Right Split

number = 2
percentage = 50.9
print(number**2)
print(percentage**2)
Message = "Hello World"
number = str(number)
print(Message+number+" Chapter 2")

print(99/2)

print("------------LIST-----------------")
bicycle = ['trek','cannodale','resline','specialized']
print(bicycle)
print(bicycle[0])
print(bicycle[2].title())
print(len(bicycle))
for cycles in range(0,len(bicycle)):
    print(bicycle[cycles].title()+" Title Case")
    print(bicycle[cycles].upper()+" Upper Case")

print("--------Excercise---3.1-----------")
names = ["Shaoib","Alauddin","Ali","Muhammad","Bilal","Qaseem"]
for name in range(0,len(names)):
    print(names[name])

print("--------Excercise---3.2-----------")
message = "Please Come to the Wedding Cermony"
for invitation in range(0,len(names)):
    print(names[invitation]+" "+message)

print("--------Excercise---3.3-----------")
transportation = ['Bus','Car','Bike','Truck','aeroplane']
print("I want to create my own "+transportation[0]+" Bussiness")
print("I want to create my own "+transportation[1]+" Bussiness")
print("I want to create my own "+transportation[2]+" Bussiness")
print("I want to create my own "+transportation[3]+" Bussiness")
print("I want to create my own "+transportation[4]+" Bussiness")

print("-------------------------------------------------------")
transportation[0] = 'Ship'
transportation.append("Trains")
print(transportation)
new = transportation.pop() # last element pop from memory |
#new = transportation.pop(len(transportation)-1)          |
print(new)
transportation.insert(3,"Long Vehicles")
print(transportation)
del transportation[len(transportation)-1]
print(transportation)
transportation.remove("Car")
print(transportation)

print("-----------------Excercise---3.4---------------------")
peoples = ["Bilal","Razi","Almeer"]
print("----------------------------------------------------")
print(peoples)
print("----------------------------------------------------")
invite = " Please Come for dinner"
print(peoples[0]+invite)
print(peoples[1]+invite)
print(peoples[2]+invite)

print("-----------------Excercise---3.5---------------------")
peoples[2] = "Mirza"
print(peoples)
print(peoples[2]+invite)

print("-----------------Excercise---3.6---------------------")
peoples.append("Zabi")
peoples.insert(0,"Rahema")
peoples.insert(2,"Junaid Qazi")
print(peoples[0]+invite)
print(peoples[1]+invite)
print(peoples[2]+invite)
print(peoples[3]+invite)
print(peoples[4]+invite)
print(peoples[5]+invite)


print("------------------Excercise--3.7------------------------")
Sorry_invitation = "Sorry you can’t invite to dinner ."
print(peoples[2]+Sorry_invitation)
print(peoples[3]+Sorry_invitation)
print(peoples[4]+Sorry_invitation)
print(peoples[5]+Sorry_invitation)
peoples.pop()
peoples.pop()
peoples.pop()
peoples.pop()
print("----------------------------------------------------")
print("New Invitation for only two last people of the list")
print("----------------------------------------------------")
new_invitation = "You are still invited"
print(peoples[0]+" "+new_invitation)
print(peoples[1]+" "+new_invitation)
print("----------------------------------------------------")
print("Empty list of invited peoples")
print("----------------------------------------------------")
del peoples[0]
del peoples[1]
print(peoples)