def bisection_method(func, a, b, tolerance, max_iterations=100):


    if func(a) * func(b) > 0:
        raise ValueError("Initial values do not have opposite signs. Bisection method requires this condition.")

    
    iteration = 0

    print(f"Iteration\t   a\t\t   b\t\t   c\t\t  f(c)")
    print("-" * 60)

    while iteration < max_iterations:
    
        c = (a + b) / 2

      
        print(f"{iteration + 1:4d}\t\t{a:.6f}\t\t{b:.6f}\t\t{c:.6f}\t\t{func(c):.6f}")


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

  
    a = float(input("Enter the lower bound of the interval (a): "))
    b = float(input("Enter the upper bound of the interval (b): "))


    epsilon = float(input("Enter the tolerance (epsilon): "))

   
    try:
        root, iterations = bisection_method(user_func, a, b, epsilon)

        print("-" * 60)
        print(f"Root found: {root}")
        print(f"Iterations performed: {iterations}")

    except ValueError as e:
        print(e)
