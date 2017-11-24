# for numbers in range(1,100):
#     if numbers%7==0 and numbers%13==0:
#         print("Divided by 7 and 13 is:",numbers)
#
# record = ["hello","world"," "]
# word =[]
# sentence =input("Please Enter any sentence")
# words = sentence.split(" ")
# print(words)
# for word in words:
#     if record
# # for word in range(0,len(sentence)):
# #     print(sentence[word])
# #
# #     if sentence[word] == " " :
# #         word
# count = []
# for w in words:
#     if w in count:
#         count[w]+=1
#     else:
#         count[w]=1
#
# print(count)


# sentence = input("Pleas ENter any sentence : ") #string literal
# # print(sentence[::-1])
# #
# # print(sentence[::2])
# vowel = ['a','e','i','o','u']
# for vowels in sentence:
#     if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'u' or vowels == 'o':
#         print("Vowels",vowels)


# pre define functions(reqiured aurgement,optional)
# dafault functions (Has no aurgument)
# User define functions(reqiured aurgement,optional)
# username = input("Please Enter your Name: ")
# def userName(username):
#     print("Hello World",username.title())

# userName(username)

# x = [10,20,30]
# cp = x.slice[:]
# # A = int(input("A :"))
# # B = int(input("B :"))
# def add(cp):
#     cp[0]=10



# print(add(cp))
#
# print(x)

# word = ['Hello',"world","pakistan"]
# for wor in word:
#     print(wor)
#     if "Hello" in wor:
#         print(wor[::-1])

# def test(a,b="Hello World"):
#     return a," ",b
#
# print(test("pakistan"))
# print(test("pakistan","Hello"))
# print(test(b="Zindabad",a="pakistan"))
# print(test("pakistan","Zindabad"))

# def build_person(first_name,Last_Name):
#     person = {'first':first_name,"Last Name":Last_Name}
#     return person
# userName = build_person("Shoaib","Alauddin")
# print(userName,"Hello World")

# list are passing by pass reference
#Preventing a Function from Modifying a List

# def make_pizza(size,**pizzas):
#     print(size,pizzas)
#
# make_pizza(25,"Hello World","Pakistan","Zindabad")
# make_pizza("Hello World","Pakistan","Zindabad","Peproni")

# * is used for tuples
# ** while is used for dictionary
#
# def make_pizza(size,**pizzas):
#     print(size,pizzas)
# print(make_pizza(25,Name="Shoaib",Age=25,roll_no=23))

def new_function(*Numbers):
    total = 0
    maximum = max(Numbers)
    minimum = min(Numbers)
    for number in Numbers:
        total+=number

    return total,maximum,minimum

number = new_function(10,2,30,40,50,60,70,80,30,50)
print(new_function(10,2,30,40,50,60,70,80,30,50,))
#
# def Dic(**list):
#     print(list)
#
# l1 = [1,2,3,4,5,6]
# l2 = [6,7,8,9,10,11]
# l3 = [10,5,20,3,50]
# print(list1=l1,list2=l2,list3=l3)