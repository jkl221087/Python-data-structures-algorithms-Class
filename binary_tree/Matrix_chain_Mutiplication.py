p = [10, 20, 5, 15, 30]

n = len(p) - 1 # 4

matrix = [[0] * (n + 1) for _ in range(n + 1)]

satrix = [[0] * (n + 1) for _ in range(n + 1)]

for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        matrix[i][j] = float('inf')
        for k in range(i, j):
            q = matrix[i][k] + matrix[k + 1][j] + p[i-1] * p[k] * p[j]
            if q < matrix[i][j]:
                
                matrix[i][j] = q
                satrix[i][j] = k


print("最小乘法次數矩陣 (matrix):")
for row in matrix[1:]: print(row[1:])
print("\n最佳分割點矩陣 (satrix):")
for row in satrix[1:]: print(row[1:])

#[10 20 5 15 30]
# l = 2 i = 1 j = 2 1 - 2 = 0
# 1 2
#q = 1 1 2 2 0 1 2 = 0 0 10*20 * 5 = 1000
# l = 3 i = 2 j = 4
# 2~4
# q = 2 2 + 3 4 + 1 + 2 + 4 = 0 + 5*15*30 + 20*5*30 = 5250
# l = 3 i = 3 j = 5
# 3 ~ 5


#時間複雜度 O(n^3)

