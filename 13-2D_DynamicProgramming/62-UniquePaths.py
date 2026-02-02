# In unique paths recursion, (Gemeral case)right path will give you a num of ways to reach the goal and left path will you a num of ways to reach the goal we need to sum to find total num of ways to reach goal.

# Recursion
# TC=2^(m*n), SC = m-1+n-1=m+n-2(Recurson stack length(path length here))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            
            right = paths(i+1,j)
            down = paths(i,j+1)

            return right + down
        
        return paths(0,0)

# Memoization DP
# TC = m*n, SC = m+n-2+(m*n)[Recursion path length + dp arr space]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def paths(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            right = paths(i+1,j)
            down = paths(i,j+1)

            dp[i][j] =  right + down
            return dp[i][j]
        
        return paths(0,0)

# Tabulation DP
# Follow steps to convert memoization to tabulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n) for _ in range(m)]
        # we have n+1 and m+1 to avoid error in the first loop down below
        # Base Case
        # Copy this base case from memoization
        # dp[m-1][n-1] = 1

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
               if row == m-1 and col == n-1:
                   dp[row][col] = 1
                   continue
               right = dp[row+1][col] if row < m-1 else 0 
               down =  dp[row][col+1] if col < n-1 else 0
               dp[row][col] = right + down
        
        return dp[0][0]

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3,7))
    print(s.uniquePaths(3,2))