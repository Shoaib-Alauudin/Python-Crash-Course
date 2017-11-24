# # def make_hirt(ize,meage):
# #     print("ize of hirt ",ize)
# #     print("entence to be printed ",meage)
# # make_hirt(20,"Hello World")
# # make_hirt(meage="Hello Python",ize = 20)
# # make_hirt("hello World",20)
# #
# # def make_hirt(ize,meage = "I love pyhton"):
# #     print(meage)
# #     print(ize)
# #
# # make_hirt("Larger","hello Pyhton")
# #
#
# # Excercie 8-12 PG NO: 187
# def sandwiche(*items):
#     for item in items:
#         print(item)
#
# print("---------------Ingredients-----------------")
# sandwiche('kabab','Egg',"Olive")
# print("---------------Ingredients-----------------")
# sandwiche("vegatable","spice","Ketchup")
# print("---------------Ingredients-----------------")
# sandwiche("Mayo","chicken","butter")
#
# print("--------------Modules---------------------")
# # Modules(collections of classes and functions)
#
# # Make_pizza calling
# import Make_pizza as mp
# mp.make_pizza(20,"Olive")
#
#
# Calculator calling
from Calculator import calculator as cal
first = int(input("First Number :"))
second = int(input("Second Number :"))
cal(first,second)
#
# print("---------------Genetors---------------")
# # Genetor is used for store a previous value
# def divby7():
#     for i in range(0,1000):
#         if i%7==0 and i%13==0:
#             yield i

#
# gen = divby7()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))