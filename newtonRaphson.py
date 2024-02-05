def newton_raphson(func, func_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = func(x)
        if abs(fx) < tol:
            return x
        x -= fx / func_prime(x)
    return x


equation = input("Enter the equation in terms of 'x' (e.g., 'x**2 - 4'): ")
func = lambda x: eval(equation)
func_prime = lambda x: (func(x + 1e-6) - func(x)) / 1e-6


x0 = float(input("Enter the initial guess (x0): "))
tolerance = float(input("Enter the tolerance: "))


result = newton_raphson(func, func_prime, x0, tol=tolerance)


print(f"Root of the equation is approximately: {result}")
