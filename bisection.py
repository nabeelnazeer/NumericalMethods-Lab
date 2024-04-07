
import math

def inp_func():
    expression = input("enter the funcyion 'eg: 5x**2-3*x+7 ': ")
    return lambda x: eval(expression)

def bisetion(f, a, b, tol = 1e-6, max_iter = 100):
    if f(a)*f(b) > 0:
        raise ValueError("the function must have opposite sign on each end point")
    
    iterations = 0
    while (b-a)/2 < tol and iterations < max_iter:

        c = (a+b)/2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations+=1
    return (a+b)/2


print("Enter the function")

f = inp_func()

a = float(input("enter the first interval: "))
b = float(input("enter the second interval: "))

tol = float(input("enter the min tolerance: "))
iter = int(input ("enter the max no. of iteration: "))

root = bisetion(f, a, b, tol, iter)

print("the root of equation is: ", root)