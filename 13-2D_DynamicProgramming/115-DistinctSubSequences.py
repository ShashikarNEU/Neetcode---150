# EASY FOR HARD PROBLEM
# Same logic as com sum but instead of having (arr) and puuting it in arr and removing it for every index, take(i,j) [i pointer for s, j pointer for t], and compare them
# if letters are same then, do (i+1,j+1)#Take else (i+1,j)#Leave. Termination codn is j has to reach end return 1 else if i==m and j != n return 0.

# Recursion
# TC = 2^(m), SC = m(Recursion Stack)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        def numD(i,j):
            if j == n:
                return 1
            if i == m and j != n:
                return 0
            res = 0
            if s[i] == t[j]:
                res += numD(i+1,j+1)
            res += numD(i+1,j)
            return res
        return numD(0,0)

# Memoization DP
# TC = m*n, SC = (m*n) + m (Rec stack)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def numD(i,j):
            if j == n:
                return 1
            if i == m and j != n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            if s[i] == t[j]:
                res += numD(i+1,j+1)
            res += numD(i+1,j)
            dp[i][j] = res
            return dp[i][j]
        return numD(0,0)

# Tabulation DP
# TC = m*n, SC = m*n
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if j == n:
                    dp[i][j] = 1
                    continue
                if i == m and j != n:
                    dp[i][j] = 0
                    continue
                
                res = 0
                if s[i] == t[j]:
                    res += dp[i+1][j+1]
                res += dp[i+1][j]
                dp[i][j] = res
                            
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.numDistinct("rabbbit","rabbit"))
    print(s.numDistinct("babgbag","bag"))