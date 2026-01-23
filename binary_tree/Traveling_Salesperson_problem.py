cost_matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]


#從城市1出發經過所有城市恰好一次最後回到城市1找出最短路徑

n = len(cost_matrix)

memo = [[-1] * (1 << n + 1) for i in range(n + 1)]



def fun(i, mask):

    if mask == ((1 << i) | 3):# i = 2 , 1 = 00001 -> 00100 | 3 = 00011 = 00111 = 城市2跟1之間沒有去過任何城市所以就剛好是最短距離
        return cost_matrix[0][i - 1]# = 10

    if memo[i][mask] != -1:# 
        return memo[i][mask]



    res = 10**9
    for j in range(1, n + 1): #1 ~ 5
        if (mask & (1 << j)) != 0 and j != i and j != 1:# 11111 & 00100 不能再重複 不能在原地
            res = min(res, fun(j, mask &(~ (1 << i)))) + cost_matrix [j - 1][i - 1] # 前一個j到 i的最小直 不斷迴圈
    
    memo[i][mask] = res #更新memo res 
    return res



full_mask = (1 << (n + 1)) - 1 

ans = 10**9

for i in range(2, n + 1):# 2 - 5
    res = fun(i, full_mask)
    ans = min(ans, res + cost_matrix[i - 1][0])

print("The cost of most efficient tour = " + str(ans))

