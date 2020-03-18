

def exponentiate(x,y):
 # Returns the value of the first integer raised to the power of the second integer.
 return (x ** y)


def raise_to_fourth_power(x):
 return exponentiate(x, 4)


square = lambda x: x ** 2

cube = lambda x: exponentiate(x,3)

print(square(2))

print(cube(2))

print(raise_to_fourth_power(2))
