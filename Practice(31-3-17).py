cars = ['bmw','audi','toyota','subaru']
print("---------------------------------------")
print("Permenent Sorted function in memory")
print("---------------------------------------")
cars.sort(reverse=False)
print(cars)
cars.sort(reverse=True)
print(cars)
print("---------------------------------------")
print("Temporary Sorting Functions")
print("---------------------------------------")
print(sorted(cars))
print("---------------------------------------")
print(cars)
cars.reverse()
print(cars)
print(len(cars))

print("----------------------Excercise--3.8--------------------------")
locations = ["USA",'Australia',"Canada",'Turkey',"Misar"]
print(locations)
print("------------------Sorted list-----------------")
print(sorted(locations))
print("------------------Original list-----------------")
print(locations)
print("------------------Sorted in a Reversed list-----------------")
locations.reverse()
print(locations)