def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def calculatedifference(x, y):
    n = len(y)
    diff = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diff[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
    return diff

def interpolate(x, y, value, diff):
    n = len(x)
    h = x[1] - x[0]
    u = (value - x[0]) / h

    result = y[0]
    for i in range(1, n):
        prod = 1
        for j in range(i):
            prod *= (u - j) / (j + 1)
        result += (prod * diff[0][i]) / fact(i)

    return result


n = int(input("Enter the number of data points: "))
x = []
y = []
for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    y_val = float(input(f"Enter y[{i}]: "))
    x.append(x_val)
    y.append(y_val)


diff = calculatedifference(x, y)


value = float(input("Enter the value for interpolation: "))
estimated_value = interpolate(x, y, value, diff)
print("Estimated value at", value, "is", estimated_value)
