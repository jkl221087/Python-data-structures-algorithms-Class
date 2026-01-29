def fib (n, memo = {}):
    if n in memo:
        return memo[n]
    
    if(n <= 2):
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

f = fib(n = 50)
print(f)

#高度m

#memo
#{
#3:2
#4:3
#5:5
#6:8
#}
#不用loop整棵樹 顯性往上成長 每一個點都有左跟右所以是2n O(n)
# 空間也是O(n) 每一次回傳都會POP所以最多也就是n O(n)