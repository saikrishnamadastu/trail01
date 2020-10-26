# range function gives values from first value to last value -1
for x in range(1,21):
	print(x)
numbers=list(range(1,15)) #list & range functions can be used to create any numerical list 
print(numbers)
# can make the values with step as well
odd_numbers=list(range(3,30,3))
print(odd_numbers)

#
squares=[]
for x in range(1,10):
	squares.append(x**2)
print(squares)
print(min(squares),max(squares),sum(squares)) 
# Print statement can have can number of values
# min, max, sum are simple builtin functions

## List comprehensions
cubes=[x**3 for x in range(1,11)]
print(cubes)