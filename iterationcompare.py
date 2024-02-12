import math

def newton_raphson(func, func_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = func(x)
        if abs(fx) < tol:
            return x
        x -= fx / func_prime(x)
    return x

def false_position_method(func, a, b, tolerance=1e-6, max_iter_ratio=1.5):
    if func(a) * func(b) > 0:
        raise ValueError("Initial values do not have opposite signs. False Position method requires this condition.")

    max_iterations = int(max_iter_ratio * (math.log(b - a) - math.log(tolerance)) / math.log(2))

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

def bisection_method(func, a, b, tolerance=1e-6, max_iter_ratio=1.5):
    if func(a) * func(b) > 0:
        raise ValueError("Initial values do not have opposite signs. Bisection method requires this condition.")

    max_iterations = int(max_iter_ratio * (math.log(b - a) - math.log(tolerance)) / math.log(2))

    iteration = 0

    while iteration < max_iterations:
        c = (a + b) / 2

        if abs(func(c)) < tolerance:
            return c, iteration

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    raise ValueError("Bisection method did not converge within the specified number of iterations.")

if __name__ == "__main__":
    equation_str = input("Enter the equation (use 'x' as the variable): ")

    def user_func(x):
        return eval(equation_str, {'x': x})

    x0 = float(input("Enter the initial guess for Newton-Raphson method (x0): "))
    tolerance = float(input("Enter the tolerance: "))

    try:
        nr_result = newton_raphson(user_func, lambda x: (user_func(x + 1e-6) - user_func(x)) / 1e-6, x0, tol=tolerance)
        print(f"Newton-Raphson method result: {nr_result}")

        a = float(input("Enter the lower bound of the interval for False Position and Bisection methods (a): "))
        b = float(input("Enter the upper bound of the interval for False Position and Bisection methods (b): "))

        false_position_result = false_position_method(user_func, a, b, tolerance=tolerance)
        print(f"False Position method result: {false_position_result}")

        bisection_result = bisection_method(user_func, a, b, tolerance=tolerance)
        print(f"Bisection method result: {bisection_result}")

    except ValueError as e:
        print(e)
