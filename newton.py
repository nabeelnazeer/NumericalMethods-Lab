
def inp_func():
    expression = input("Enter the function 'eg: x**3-2*x-4': ")
    return lambda x: eval(expression)

def newton(f, f_1, x0, max_iter = 100, tol = 1e-6):
    iterations = 0
    while iterations < max_iter:
        x1 = x0 - f(x0)/f_1(x0)
        if abs(x1-x0) < tol:
            return x1
        else:
            x0 = x1
        iterations += 1
    raise ValueError("Did not converge")

def main():
    # Get user input for the function
    f = inp_func()

    # Get the derivative of the function using numerical differentiation
    h = 1e-6  # Step size for numerical differentiation
    f_1 = lambda x: (f(x + h) - f(x)) / h

    # Get user input for initial guess and maximum number of iterations
    x0 = float(input("Enter initial guess: "))
    max_iter = int(input("Enter maximum number of iterations: "))
    tol = float(input("Enter tolerance: "))

    # Call the newton function
    root = newton(f, f_1, x0, max_iter, tol)

    print("Approximate root:", root)

if __name__ == "__main__":
    main()        