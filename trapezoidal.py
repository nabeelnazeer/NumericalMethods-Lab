def trapezoidal(x, y):
    h = x[1] - x[0]

    middle_term_2 = 0

    for i in range(1, len(x) - 1):
        middle_term_2 += y[i]


    result =     (h/3)*(y[0] + 2*(middle_term_2) + y[len(y)- 1]) 
    return result

x = list(map(float, input("enter values of x (Space seperated)").split()))
y = list(map(float, input("enter values of y (Space seperated)").split()))

print(trapezoidal(x,y))
