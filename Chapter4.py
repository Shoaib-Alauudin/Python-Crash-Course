# Looping through entire list
magicians = ['Alice',"Khan","Ali","Noman","zabi"]
for magicain in magicians:
    print(magicain.title().upper().lower())
print(magicain.upper())

# Range function
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List Comprehensions Chapter 4
squares = [value**2 for value in range(1,11)]
for square in squares:
    print(square)
print(squares)

sums = [value for value in range(1,1000001)]
print(min(sums))
print(max(sums))
print(sum(sums))

# Slicing the list
numbers = [value for value in range(1,12)]
perticularNumbers = numbers[:]
print(perticularNumbers)
numbers.append(90)
perticularNumbers.append(40)
print(numbers)
print(perticularNumbers,"\n")

print(numbers[3::2])
print(numbers[-8:9:3])
print(numbers[-9:9])
print(numbers,"\n")

# Tuples (Variables that can not be changes):
dimensions = (1,2,3,4,5,6)
print(dimensions,"\n")
# dimensions[3] = 6 (Can not change ones assign)
# Tuples can overwrite instead of change
dimensions = (10,20,30,40,50,60)
print(dimensions,"\n")
