# # Scrapy is used to extract data from diffrent websites
# class point():
#     def __init__(self,x,y):
#         self._x = x
#         self._y = y
#
#
#
# class Shape():
#     print("Drawing In shape class")
#     def __init__(self,area):
#         self.Area = area
#     def draw(self):
#         print("Drawing Shapes.")
#
#
# class Rectangle(Shape):
#     def __init__(self,top_left,bottom_right,area):
#         super().__init__(area)
#         self.top_left = top_left
#         self.bottom_right = bottom_right
#
#     def draw(self):
#         print("Draw by Rectangle class.")
#
# class Triangle(Shape):
#     def __init__(self,v1,v2,v3,area):
#         super().__init__(area)
#         self.v1 = v1
#         self.v2 = v2
#         self.v3 = v3
#
#     def draw(self):
#         print("Draw by triangle class.")
#
#
# p1 = point(10,5)
# p2 = point(15,10)
# p3 = point(5,10)
#
#     # composition (object of one class is used in another class)
#
#
# r1 = Rectangle(p1,p2,10)
# r1.draw()
#
# t1 = Triangle(p1,p2,p3,area=20)
# t1.draw()

print("--------------Exception Handling----------------")
try:
    with open('xyz') as file_object:
        content = file_object.read()

except :
    print("This file is not in your directry")
else:
    print("When exception not occurs")

finally:
    print("Sorry Exception occurs")
#   Data science from scrach pdf






