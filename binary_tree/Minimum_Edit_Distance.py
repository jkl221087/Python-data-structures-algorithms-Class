x = "kitten"
y = "sitting"

n, m = len(x), len(y)

# 刪除 替換 插入

matrix = [[0] * (m + 1 ) for _ in range(n + 1)]

for i in range(n + 1):
    matrix[i][0] = i

for j in range(m + 1):
    matrix[0][j] = j



for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i - 1] == y[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1]#字串相同就不用處理
        else:
            matrix[i][j] = min(matrix[i - 1][j] + 1, #刪除
                            matrix[i - 1][j - 1] + 1, #替換
                            matrix[i][j - 1] + 1)#插入

print(f"最小編輯距離為: {matrix[n][m]}")