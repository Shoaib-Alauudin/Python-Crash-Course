'''print("------Assignment-------------")
names = ["Ali ","Khan "]
print(names)
message = "Come for dinner"
print(names[0]+message)
print(names[1]+message)
names.append("Muhammad")
print(names)
print(names[2]+message)
names[0] = "Zabi"
print(names)
names.pop(0)
print(names)


print("--------------------------------------------")
magicians = ["alice","david","Calirina"]
for magician in magicians:
    print(magician)


print("--------------------------------------------")
for value in range(10,1,-3):
    print(value)

print("--------------------------------------------")
cars = ["Bmw","Farari","Honda","Ducati"]
for car in range(cars[0],cars[len(cars)-1]):
    print(car) '''

'''print("--------------------------------------------")
square = []
for values in range(0,11):
    print(values**2)
    square.append(values**2)
print(square)


print("--------------------------------------------")
num = [1,2,3,4,5,6,7,8,9,10]
newList = [n+1 for n in num]
print(newList)

print("--------------------------------------------")
for num in range(0,100,15):
    print(num)


print("--------------------------------------------")
list = [numb for numb in range(0,100,15)]

print(list)

print("--------------------------------------------")
listNew = list(range(0,1000,15))
print(listNew)'''


'''names = ['ahmed','moazzam','ahmed']
for name in names:
            print(name +       " hutiya." + ".")'''

#for value in range(1,10):
 #   print(value)
a = list(range(1,10))
print(a)

numbers = [n+1 for n in a ]
print(numbers)

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#    print(magician.title() + ", that was a great trick!")
#    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# deep coping (slicing is used for deep coping)
# shalow coping


#fruits = ["Apples","Orange","Banana","Mango"]
#new_fruits = fruits[:]
#fruits.append("blueberry")
#print(fruits)
#print(new_fruits)

print("------------------slicing---------4-10:-----------------")
a = ['a','b','c','d','e','f','g']
message = "List of Alpha.."
A = a[:3]
print(A)
b = int(len(a)/2)
B = a[(b-1):(b+2)]
print(B)
C = a[-3:]
print(C)

print("------------------------Tuples---------------------------")
# tuples used as a Contant
# We can't change the value of tuple
#

A = list(range(0,100))
print(A)
B = tuple(A)
print(B)
# B.append(1,0,1) ----> Cause of Error
# print(B)


print("----------------------Conditional-----------------------")
# pyhton doesn't support swich condition
age = 18
print(age == 18)
# Operators (and ,or, not)

PlayingEleven = ["Afridi","Yunis","Saeed Anwer","Shoaib Malik"]
# for players in PlayingEleven:
if "Misbah" in PlayingEleven:
    print("Pakistan will Lose")
elif "Afridi" in PlayingEleven:
    print("Pakistan will Lose")
else:
    print("Pakistan Will Win the match")

print("------------------------------------------------")

for players in PlayingEleven:
    if "Misbah" or "Afridi" == players:
        print("Pakistan will Lose")
        break
    else:
        print("Pakistan will win")


# list compehension (players Examples)