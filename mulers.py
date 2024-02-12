
import cmath


# def defined_function(x):
#     return eval(function)

# def evaluate(func, value):

#     result = func(value)
#     return result
def mulers(func, x0, x1, x2, iter):

    for i in range (iter):
        h0 = x1-x0
        h1 = x2-x1
        f0 = func(x0)
        f1 = func(x1)
        f2 = func(x2)
        d0 = (f1-f0)/h0
        d1 = (f2-f1)/h1
        a = (d1 - d0)/(h0+h1)
        b = a*h1 + d1
        c = f2

        discriminant = cmath.sqrt(b**2 - 4*a*c)

        if abs(b + discriminant) > abs(b-discriminant):
            den  = b + discriminant
        else:
            den = b - discriminant

        dxr = -2*c / den
        x3 = x2 + dxr

        relative_error = (abs (x3-x2)/ abs (x3)) * 100

        if relative_error < 1e-6:
            return x3, i
        x0, x1, x2 = x1, x2, x3

    return x3, iter


function = input('Enter the function expression in terms of x  : ')
x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
iter = int(input("Enter the number of iterations: "))

func  =  eval("lambda x : " + function)

root, iterations = mulers(func, x0, x1, x2, iter)

if root is not None:
    print(f"Root found at {root} after {iterations} iterations.")
else:
    print(f"No root found after {iterations} iterations.")
