#write a program to  estimate the value of a function for any intermediate value of the independant vriable using newton forward interpolation method


def fact(n):
    f = 1;
    for i in range(2 , n+1):
        f *= i;
        return f;


def calculatedifference(x,y):
    n = len(y)
    diff = [[0 for _ in range(n)] for _ in range (n)]

    for i in range(n):
        diff[i][0] = y[i]

    for j in range(1,n);
        for i in range():
            diff[j][i]     


