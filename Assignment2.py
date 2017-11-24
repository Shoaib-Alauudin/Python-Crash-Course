message = "I love"
foods = ["Biryani","Nahari","Pai","Palao","Qorma","Haleem","Zinger"]
for food in foods[0:3]:
    print(message+" "+food)
print("-------------------------------------------------------------")
range = int(len(foods)/2)
for food in foods[range-1:range+2]:
    print(message+" "+food)

print("-------------------------------------------------------------")
for food in foods[-3:]:
    print(food)

print("-----------------------Excercise-4.11-----------------------------")
My_pizzas = ["Chesse Pizza","Chicken Pizza","Fajeta","Italic","Vegatable","Beef Pizza"]
Your_Pizzas = My_pizzas[:]
My_pizzas.append("Garlic")
Your_Pizzas.append("BBQ pizza")

print(My_pizzas)
print(Your_Pizzas)


print("----------------------Excercise-4.13------------------------------")
Dishes = ("Biryani","Nahari","Qorma","Pizza","Tikka")
print(Dishes)


print("-----------------------------------------")
topping = []

