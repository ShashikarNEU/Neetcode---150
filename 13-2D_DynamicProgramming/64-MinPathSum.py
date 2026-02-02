# In min cost sum recursion, (General case)right path will give you a cost to reach the goal and left path will you a cost to reach the goal we don't need to sum it(WRONG), we take min of both the paths and return it.

# Recursion
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def minPaths(i,j):
            if i > m-1 or j > n-1:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            
            rightCost = grid[i][j] + minPaths(i+1,j)
            
            downCost = grid[i][j] + minPaths(i,j+1)
            
            minCost = min(rightCost, downCost)
            return minCost
        return minPaths(0,0)

# Recursion - using for loop
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[0,1]]
        
        def minPaths(i,j):
            if i > m-1 or j > n-1:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            minCost = float('inf')
            for r,c in directions:
                cost = grid[i][j]+minPaths(i+r,j+c)
                minCost = min(cost, minCost)
            return minCost
        
        return minPaths(0,0)

# Memoization DP
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]

        def minPaths(i,j):
            if i > m-1 or j > n-1:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            rightCost = grid[i][j] + minPaths(i+1,j)
            
            downCost = grid[i][j] + minPaths(i,j+1)
            
            dp[i][j] = min(rightCost, downCost)
            return dp[i][j]
        return minPaths(0,0)

# Tabulation DP
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                # Base case
                if row == m-1 and col == n-1:
                    dp[row][col] = grid[row][col]
                    continue
                
                rightCost = grid[row][col] + dp[row+1][col] if row < m-1 else float('inf')
            
                downCost = grid[row][col] + dp[row][col+1] if col < n-1 else float('inf')

                dp[row][col] = min(rightCost, downCost)
        
        return dp[0][0]
                
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))