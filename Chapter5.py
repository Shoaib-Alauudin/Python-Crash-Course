cars = ('bmw','audi','subaru','farari','toyota','farari')
car = 'honda'
if 'farari' in cars:
    print(cars.index('farari'))
    print(cars.count('farari'))

if car not in cars:
    print("Sorry Honda not in tuples")

requested_topping = ['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("\nAdding mushrooms")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")

names = []
if names:
    print('List empty')

