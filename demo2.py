def remove_element(nums, val):

    for i in range(len(nums) -1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    
    return len(nums)

nums = [1, 1, 1, 1, 1]
val = 1
k = remove_element(nums, val)

print(f"剩餘數量: {k}")         # 輸出: 0
print(f"前 k 個元素: {nums[:k]}") # 輸出: []