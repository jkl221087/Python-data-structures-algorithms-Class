def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

def memoziation_gridTraveler(m, n, memo = {}):
    key = str(m) + ',' + str(n)

    if key in memo:return memo[key]

    if m == 1 and n == 1:return 1
    if m == 0 or n == 0:return 0

    memo[key] = memoziation_gridTraveler(m - 1, n, memo) + memoziation_gridTraveler(m, n - 1, memo)
    return memo[key]


m = memoziation_gridTraveler(m = 18,n = 18)
print(m)
#m-1 or n - 1
#
#高度 m * n
#O(2^n + m)time
#O(n + m)space
#都是二叉數 代表一個節點會有兩個子節點 n + m


#memoziaiton dp 優化

#memo{}

#