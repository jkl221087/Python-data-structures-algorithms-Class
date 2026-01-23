n = 5
p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

e = [[0.0] * (n + 2) for _ in range(n + 2)]

w = [[0.0] * (n + 2) for _ in range(n + 2)]

root = [[0] * (n + 2) for _ in range(n + 2)]



for i in range(1, n + 2):
    e[i][i - 1] = q[i - 1]
    w[i][i - 1] = p[i - 1]



for l in range(1, n + 1):# 1
    for i in range(1, n - l + 2):# 1
        j = i + l - 1# 1 + 1 - 1 = 1
        e[i][j] = float('inf')
        w[i][j] = w[i][j - 1] + p[j] + q[j] #w11 = w10 + p1 + p1
        print( w[i][j])
    
        for r in range(i, j + 1):
            t = e[i][r - 1] + e[r + 1][j] + w[i][j]

            if t < e[i][j]:
                e[i][j] = t
                root[i][j] = r

print(f"最小搜尋成本: {e[1][n]}")