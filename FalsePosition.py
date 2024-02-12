def false_position_method(func, a, b, tolerance=1e-6, max_iterations=100):
    if func(a) * func(b) > 0:
        raise ValueError("Initial values do not have opposite signs. False Position method requires this condition.")

    iteration = 0

    while iteration < max_iterations:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if abs(func(c)) < tolerance:
            return c, iteration

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    raise ValueError("False Position method did not converge within the specified number of iterations.")

if __name__ == "__main__":
    # Define the function for x**3 - 4x - 9
    def user_func(x):
        return x**3 - 4*x - 9

    a = float(input("Enter the lower bound of the interval (a): "))
    b = float(input("Enter the upper bound of the interval (b): "))

    try:
        root, iterations = false_position_method(user_func, a, b)

        print(f"Root found: {root}")
        print(f"Iterations performed: {iterations}")

    except ValueError as e:
        print(e)
