def longestPalindrome(s:str):
    result = ""
    length = len(s)

    dp = [[False] * length for _ in range(length)]
    for i in range(length):# 0 1 2 3
        for j in range(i + 1):# 0 0 1 0 1 2 0 1 2 3
            if i - j == 0:dp[i][j] = True
            elif i - j == 1: dp[i][j] =(s[i] == s[j])
            else:
                dp[i][j] = (dp[i - 1][j + 1] and (s[i] == s[j]))
            if dp[i][j] and i - j + 1 > len(result):
                result = s[j:i+1]
    return result

l = longestPalindrome(s = "babad")

print(l)

# i = 0
# j = 0 + 1
# 0 1  =
#True False False False 
#False True False False 
#True False True False 
#False True  False True 
#放進result = "a"
#