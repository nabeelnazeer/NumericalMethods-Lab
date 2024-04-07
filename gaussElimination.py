def gaussElimination(A, b):
    n = len(b)

    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            