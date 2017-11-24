
'''
def Student_data(Name,Age,Roll_no=124,CGPA=3.8):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Roll Number : ",Roll_no)
    print("CGPA : ",CGPA)

Student_data("Shoaib",23,CGPA=3.7)
Student_data(Name="Rahema Kamal",Age=18,CGPA=4.00)

'''

'''
# function Returns a dictionary and a list

polls_results = {}
polls = []
def checking_function(Name,Comment):
    polls_results[Name]=Comment
    polls.append(Name)
    polls.append(Comment)
    return polls,polls_results

'''

'''
final_polls_results = {}
final_results = []
final_polls_results = checking_function("Shoaib","I love python")
final_results = checking_function("Rahema Kamal","She Want to be a doctor")
print("Dictionary : ",final_polls_results)
print("List : ",final_results)

'''

'''
def get_formatted_name(first_name,last_name):
    full_name = first_name+" "+last_name
    return full_name
name = get_formatted_name("Shoaib","Alauddin")
print(name)

'''

#
# flag = True
# while flag:
#     print("Please tell me your name: ")
#     f_name = input("First Name : ")
#     l_name = input("Last Name : ")
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(formatted_name)
#     user = input("Do you want to continue? (yes/No)")
#     if user == "No":
#         flag = False

'''
Name_lists = []
def lst(names):
    for name in names:
        Name_lists.append(name)
Names = ["Shoaib","Rahema","Wajeeha","Rahat","Masoom","Mami","Dadi"]
lst(Names)
print(Name_lists)

checking_models = []
def print_model(unprinted_design,complete_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        complete_models.append(current_design)
    return complete_models

working on the original old_design list (pop() is used for removing in the memory)
print("--------Function return-> Checking Model----------")
checking_models = print_model(old_design,new_models)
print(checking_models)
print("-------------old Models---------")
print(old_design)

'''

'''
checking_models = []
def print_model(unprinted_design,complete_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        complete_models.append(current_design)
    return complete_models

old_design = ["hello1","Python","World","Machine Deep learning"]
new_models = []

# Slicing the old_design list (Copying the current design before use)
print("--------Function return-> Checking Model----------")
checking_models = print_model(old_design[:],new_models)
print(checking_models)

print("-------------old Models---------")
print(old_design)
'''

#

# def make_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
#
# make_pizza("pepperoni","Black pepper","Onion","Ketchup")
#
# print("---------------------------------")
# make_pizza("Mushroom")
#


# def build_profile(first_name,last_name,**other_informations):
#     full_name = first_name+" "+last_name
#     print(full_name)
#     for key,value in other_informations.items():
#         print("profiel [",key,"] = ",value)
#
# build_profile("SHoaib","Alauddin",roll_no = 124,gpa=3.68,cgpa=3.7,semester="8th Semester")

# from chapter8_makePizza import make_pizza as pizza
# pizza("Small",["pepproni","Mushroom","Cheese","Onion","Garlic"])
#
# from chapter8_makePizza import *
# make_pizza("large",["Pepproni","Mushroom"])
# hello_python()
# hello_world()

# def user_detail(f_name, l_name, **user_details):
#
#     profile={}
#     profile[f_name]=f_name
#     profile[l_name]=l_name
#
#     print("User Name : ", f_name, " ", l_name)
#
#     for key,value in user_details.items():
#
#
# user_detail("Shoaib",l_name="Alauddin", Age:25,location:"Karachi")
#

#
# def user_detail(f_name,l_name,**user_details):
#     print("First Name : ",f_name)
#     print("Last Name :",l_name)
#     for key, value in user_details.items():
#         print(key)
#         print(value)
# user_detail('Shoaib',l_name='Alauddin',Age=23,Location='Karachi')

import Make_pizza as piza
piza.make_pizza("Small","Peproni","Chesse","Black Pepper","Vegatable")


print("========================")

from Make_pizza import pizza as pz
pz("Large",Location="Karachi",Time="3:45 Pm",charges=1099)

print("---------------------------------------")
from Make_pizza import *
make_pizza("Small","Black pepper","Chesse","Onion")
print("=====")
pizza("Large",Location="Karachi",Time="3:45 Pm",charges=1099)