import math

def f(x):
    # Function input by the user will be evaluated here
    return eval(expression, {'x': x})

def simpsons_3_8(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 3 * f(a + i * h)
    result *= 3 * h / 8
    return result

# Taking user input for the function
expression = input("Enter the function to integrate (use 'x' as the variable): ")

# Taking input for integration limits
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))

# Taking input for the number of subintervals (must be multiples of 3)
n = int(input("Enter the number of subintervals (must be multiples of 3): "))

# Performing integration using Simpson's 3/8 rule
result = simpsons_3_8(a, b, n)
print("Result of integration using Simpson's 3/8 rule:", result)
