def inp_function():
    expression = input("Enter the function: ")
    return lambda x: eval(expression)

def false_position(f, a, b, tol, max_iter=100):
    if f(a)*f(b) > 0:
        raise ValueError("The function must have opposite sign endpoints")
    iterations = 0
    while iterations < max_iter:
        f_a = f(a)
        f_b = f(b)
        if f_a == f_b:
            raise ValueError("Function values at the endpoints are equal. Cannot proceed.")
        c = a - (f_a * (b - a)) / (f_b - f_a)
        if abs(f(c)) < tol:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    raise ValueError("Did not converge")

def main():
    a = float(input("Enter left endpoint of the interval: "))
    b = float(input("Enter the right endpoint of the interval: "))
    tol = float(input("Enter the tolerance: "))

    f = inp_function()

    root, iterations = false_position(f, a, b, tol)

    print("The root is", root, "found with", iterations, "iterations.")

if __name__ == "__main__":
    main()
