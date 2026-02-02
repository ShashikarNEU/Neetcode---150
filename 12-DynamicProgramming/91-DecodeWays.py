# Soln to question is very similar to com sum basic soln
# but think about the 0 case(if you get that then consider the question solved)
# we can consider any non zero num + 0 as a digit but if we get 0 other num or 06 other num -> not valid
# so, once if we get 0, whole seq is not valid so, if s[index] == 0: return 0

# base logic
# max length that can be taken is 2
# take one num or take two num. for taking two num check length limit(cuz of index+1) and see if the s[index:index+2] is within 1 to 26
# rest is same as before problems

# other way to check for two take digits(instaed of cat them and checking the range bw 1 to 26), we can check them seperately. first letter can be if first letter is 1, second can be anything and if first letter is 2 then second should be <=6
# if i < len(s) - 1:
#                 if (s[i] == '1' or 
#                    (s[i] == '2' and s[i + 1] < '7')):
#                     res += dfs(i + 2)
# https://neetcode.io/solutions/decode-ways

# Recursion soln
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def decode(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            res = 0
            if i+2 <= n:
                if s[i:i+2] >= '10' and s[i:i+2] <= '26':
                    res += decode(i+2)
            res += decode(i+1)
            return res
        
        return decode(0)

# Memoization DP
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)
        def decode(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            res = 0
            if i+2 <= n:
                if s[i:i+2] >= '10' and s[i:i+2] <= '26':
                    res += decode(i+2)
            res += decode(i+1)
            dp[i] = res
            return res
        
        return decode(0)

# Tabulation DP
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1

        for i in range(n-1,-1,-1):
            if s[i] == '0':
                continue
            res = 0
            if i+2 <= n:
                if s[i:i+2] >= '10' and s[i:i+2] <= '26':
                    res += dp[i+2]
            res += dp[i+1]
            dp[i] = res
        return dp[0]
                    
