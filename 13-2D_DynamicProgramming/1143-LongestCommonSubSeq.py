# LOGIC
# solving them seperately via com sum and comparing them is hard so, think for a another way
# text1 = "abcde", text2 = "ace"
# think when both i and j index letters are matching and same, then we go forward rec(i+1,j+1) and increase count by 1(1+LCS(i+1,j+1)). else if it's not same then, you try to move i by 1 or j by 1 to make them equal. so, a=rec(i+1,j) b=rec(i,j+1). now, both rec call will have outputs. for max length, return max(a,b). the termination codn is that when j or i goes out of bounds then return 0.

# for a and b, a might have ce length(2) and b might have 3 (ace) [this happened by (i+1,j),(i,j+1) rec call], so, we take the max of the two

# Recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def LCS(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1+LCS(i+1,j+1)
            a = LCS(i+1,j)
            b = LCS(i,j+1)
            return max(a,b)
        return LCS(0,0)

# Memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def LCS(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1+LCS(i+1,j+1)
            if dp[i][j] != -1:
                return dp[i][j]
            a = LCS(i+1,j)
            b = LCS(i,j+1)
            dp[i][j] =  max(a,b)
            return dp[i][j]
        return LCS(0,0)

# Tabulation
# Most of the soln is same as recursion, memoization
# one diff is what to do if text1[i] == text2[j] in that case, from res = max(dp[i+1][j],dp[i][j+1]) and take max(res, 1+dp[i+1][j+1])
# Draw the 2d matrix and build from bottom up and see why
# (i,j) (i,j+1)
# (i+1,j) (i+1,j+1)
# from this diagram, it's easy how to find dp[i][j] right?[Use Common Sense]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1]*(n+1) for i in range(m+1)]

        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                # Always put base case inside loop for tab
                if i >= m or j >= n:
                    dp[i][j] = 0
                    continue
                
                # if it's equal
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    continue

                # if it's not equal
                a = dp[i+1][j] 
                b = dp[i][j+1]

                dp[i][j] = max(a,b)
        
        return dp[0][0]
            
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde","ace"))
    print(s.longestCommonSubsequence("abc","abc"))
    print(s.longestCommonSubsequence("abc","def"))
  