# EASY FOLLOW UP TO UNIQUE PATHS
# Recursion
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def paths(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            right = paths(i+1,j)
            down = paths(i,j+1)

            return right + down
        
        return paths(0,0)

# Memoization DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        def paths(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            right = paths(i+1,j)
            down = paths(i,j+1)

            dp[i][j] =  right + down
            return dp[i][j]
        
        return paths(0,0)

# Tabulation DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        #dp[m-1][n-1] = 1
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                if row == m-1 and col == n-1:
                    dp[row][col] = 1
                    continue
                right = dp[row+1][col] if row < m-1 else 0
                down = dp[row][col+1] if col < n-1 else 0
                dp[row][col] = right + down
        return dp[0][0]
            
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
            