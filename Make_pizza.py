def make_pizza(size, *toppings):
    print("Making a ",str(size)," Inches pizza")
    print("Your topping List is Below")
    for topping in toppings:
        print(topping)

def pizza(size,**toppings):
    for key, value in toppings.items():
        print(key," : ",value)