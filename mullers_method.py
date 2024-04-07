
import numpy as np


def inp_func():
    expression = input("Enter the function : ")
    return lambda x: eval(expression)

def mullers(f, x0, x1, x2, e):
    iteration = 0
    while True:
        iteration+= 1
        h0= x1-x0
        h1 = x2- x1

        d0 = (f(x1) - f(x0))/ h0
        d1 = (f(x2) - f(x1))/ h1

        a = (d1-d0)/(h1 + h0)
        b = a*h1 + d1
        c = f(x2)

        denom = b**2 - 4*a*c

        if denom == 0:
            raise ValueError("division by zero")
    
        x3 = x2 - (2*c)/(b+ np.sqrt(denom))
    
        if abs(x3-x2)/x3 < e or iteration >= 100:
            break

        x0 = x1
        x1 = x2
        x2 = x3
    return x3, iteration
       

f = inp_func()
x0 = float(input("Enter the first guess: "))
x1 = float(input("Enter the second guess: "))
x2 = float(input("Enter the third guess: "))

E = float(input("Enter the error: "))

root, iteration = mullers(f,x0, x1, x2, E)
print("The root is: ", root)
print("The number of iterations taken is: ", iteration)
