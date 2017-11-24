# print("-----------chapter 9-----------------")
# class dog():
#
#     # object is a instance of class
#     # __init__ is instance
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title()," Is sitting now")
#     def roll_over(self):
#         print(self.name.title()," Rolled over")
#
# # Encp (data and related information are together)
# d1 = dog("Buldog",45)
# print(d1.name)
# d1.sit()
# d2 = dog("papi",10)
# print(d2.name)
# d2.roll_over()
#
# print("\n-----Student Class------\n")
# class student():
#     def __init__(self,Name,Age):
#         self.setName(Name)
#         self.setAge(Age)
#
#     def setName(self,Name):
#         self.__Name = Name
#
#     def getName(self):
#         print("Student Name :",self.Name)
#         return self.__Name
#
#     def setAge(self,Age):
#         if (Age < 0):
#             self.__Age = Age
#
#     def getAge(self):
#         print("Student Age :",self.Age)
#         return self.__Age
#
#
# st = student("Shoaib",23)
# print(st.Name)
# print(st.Age)
# st.getName()
# st.getAge()

class Dog():
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def sit(self):
        print(self.f_name.title()," is sitting now")

my_dog = Dog("Puppy","boy",5)
print(my_dog.f_name.upper())
print(my_dog.age)
my_dog.sit()


print("============================")

class car():

    def __init__(self,name,company,model,year):

        self.name = name
        self.company = company
        self.model = model
        self.year = year
        self.location = "karachi"

honda = car("Civic","honda",2011,2017)
print(honda.location)