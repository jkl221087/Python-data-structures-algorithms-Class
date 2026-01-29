def canSum(targetnum, numbers):
    if targetnum == 0:
        return True
    for num in numbers:
        reminder = targetnum -  num
        if canSum(reminder, numbers) == True:
            return True
    return False



#子樹布林傳給二元樹如果其中一個是True parent return True
#
#