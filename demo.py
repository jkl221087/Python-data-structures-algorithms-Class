cost_matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]


#從城市1出發經過所有城市恰好一次最後回到城市1找出最短路徑

n = len(cost_matrix)

# 建立 5x32 的筆記本
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]

def fun(i, mask):
    # Base Case: 當 mask 只剩下城市 i 和起點 (城市 1)
    # 代表這是旅行的第一步：1 -> i
    if mask == ((1 << i) | 3):
        return cost_matrix[0][i-1] # 索引修正：城市1是0，城市i是i-1
    
    if memo[i][mask] != -1:
        return memo[i][mask]
    
    res = 10**9

    for j in range(1, n+1):
        # 尋找前一個城市 j
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            # 遞迴：(1->...->j) 的距離 + (j->i) 的距離
            res = min(res, fun(j, mask & (~(1 << i))) + cost_matrix[j-1][i-1])
            
    memo[i][mask] = res
    return res

ans = 10**9
# 初始 Mask 是 31 (二進制 11111)
full_mask = (1 << (n+1)) - 1

for i in range(2, n + 1):
    # 算 (1...i) 的最短距離 + (i 回到 1) 的距離
    res = fun(i, full_mask)
    ans = min(ans, res + cost_matrix[i-1][0])

print("The cost of most efficient tour = " + str(ans))
# def fun (i, mask):
    
#     if mask == ((1 << i) | 3):# 001 011 = 011, 100 011 = 111
#         return cost_matrix[1][i]






cost_matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]


#從城市1出發經過所有城市恰好一次最後回到城市1找出最短路徑

n = len(cost_matrix)


memo = [[-1] * (1 << (n + 1)) for i in range (n + 1)]
print(memo)



# if i=1 than 00001 = 00010 | 00011 = 00011
# i=4 | 10000 | 10011
# full mask = 31 11111 不斷扣掉 直到 10011
def fun (i, mask):

    if mask == ((1 << i) | 3):
        return cost_matrix[0][i - 1]
    


    if memo[i][mask] != -1:
        return memo[i][mask]
    


    res = 10**9

    
    for j in range(1, n + 1):
        if(mask & (1 << j)) != 0 and j != 1 and j != 1:
            res = min(res, fun(j, mask & (~(1 << i)))) + cost_matrix[j-1][i-1]
            # 在還沒到i前 停在j的最短路徑
            #j:前一個城市
            # i是目前在的城市
            # ~ 除了城市i的位置變成 0其他所有位置都變成 1
            #res不斷的更新最短路徑
            # +cost把以前走過的j最短紀錄 + j到i的最小步
    
    memo[i][mask] = res
    return res


ans = 10**9

full_mask = (1 << (n + 1) - 1)
for i in range(2, n + 1):
    res = fun(i, full_mask)
    ans = min(ans, res + cost_matrix[i - 1][0])
