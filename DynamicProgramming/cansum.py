def canSum(targetnum, numbers):
    if targetnum == 0:
        return True
    for num in numbers:
        remainder = targetnum - num
        if canSum(remainder, numbers) == True:
            return True
    return False



def memoziation_canSum(targetnum, numbers, memo = {}):
    if targetnum in memo:return memo[targetnum]
    if targetnum == 0:return True
    if targetnum < 0:return False

    for num in numbers:
        remainder = targetnum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetnum] = True
            return True
    memo[targetnum] == False
    return False


c = memoziation_canSum(7, [7, 14])
print(c)


#casum 暴力解
#m = target num
#m = array length
#最壞情況到最低節點高度m   -1 m 次
#假設長度3的array 每一個節點都會有三個子節點 n = 3 高度m次 O(n^m) 指數成長



#memoation優化
#子樹布林傳給二元樹如果其中一個是True parent return True
#O(m * n)time
#O(m)space