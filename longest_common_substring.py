import numpy as np

x = "alccccaassddllllqoeeeeee"
y = "defefeeefsllleoooqpppppp"

m, n = len(x), len(y)


matrix = [[0] * (n + 1) for _ in range(m + 1)]
length = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if x[i - 1] == y[j - 1]:
            matrix[i][j] = matrix[i - 1][ j - 1] + 1
            length = max(length, matrix[i][j])
    else:
        matrix[i][j] = 0

print(length)