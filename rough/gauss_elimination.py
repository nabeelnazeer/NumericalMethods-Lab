def inp_func(x):
    return lambda x: eval(x)

def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]
        for j in range(n):
            if j != i:
                eq = matrix[j][i] / pivot
                for k in range(n+1):
                    matrix[j][k] -= eq * matrix[i][k]

        for j in range(n+1):
            matrix[i][j] /= pivot

    solutions = [0] * n

    for i in range(n-1, -1, -1):
        solution = matrix[i][n]
        for j in range(i+1, n):
            solution -= matrix[i][j] * solutions[j]
        solutions[i] = solution

    return solutions

def get_input(n):
    matrix = []
    for i in range(n):
        eq = input(f"Enter coefficients for equation {i+1} separated by spaces: ")
        eq = list(map(float, eq.split()))
        matrix.append(eq)
    return matrix

def main():
    n = int(input("Enter the number of equations: "))
    matrix = get_input(n)
    solutions = gauss_elimination(matrix)
    for i, solution in enumerate(solutions):
        print(f"x{i+1} =", solution)

if __name__ == "__main__":
    main()
