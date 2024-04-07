from math import e;



def f(x, func):
    return eval(func)


def simpsons(a, b, n, func):

    h = (b-a)/n

    result = f(a,func) + f(b,func)

    for i in range(2, n ,2):

        result += 4*f(a+i*h,func)


    for i in range(1, n-1, 2):

        result += 2*f(a+i*h,func)    


    result *= h/3    

    return result;  

    # Taking user input for the function
func = input("Enter the function to integrate (use 'x' as the variable): ")

# Taking input for integration limits
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))

# Taking input for the number of subintervals
n = int(input("Enter the number of subintervals (must be even): "))

# Performing integration using Simpson's rule
result = simpsons(a, b, n, func)
print("Result of integration using Simpson's rule:", result)