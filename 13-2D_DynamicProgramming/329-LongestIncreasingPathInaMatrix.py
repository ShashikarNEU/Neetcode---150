# This problem has no bottom up soln - not there in neetcode
# https://neetcode.io/solutions/longest-increasing-path-in-a-matrix
# Recursion

# Appoarch
# Basically we have to find the longest increasing path here and there exists a edge when if matrix [i][j] < matrix[i+r][j+c]
# so, what we have to do is apply DFS/Topo sort
# There won't be cycle at all so, need of visited
# 1 -> 2 -> 3 -> 1 (3>1 so, it's not possible)
# and one cache for the whole problem

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(i,j):
            max_path_dfs = 1
            
            for r,c in directions:
                if i+r < 0 or j+c < 0 or i+r >= ROW or j+c >= COL:
                    continue
                if matrix [i][j] < matrix[i+r][j+c]:
                    max_path_dfs = max(max_path_dfs, 1 + dfs(i+r,j+c))
            
            return max_path_dfs
        
        max_path = 0
        for i in range(ROW):
            for j in range(COL):
                max_path = max(max_path, dfs(i,j))
        return max_path

# Memoization DP
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        dp = [[-1]*(COL) for _ in range(ROW)]
        
        def dfs(row,col):
            if dp[row][col] != -1:
                return dp[row][col]

            max_path_dfs = 1
            for r,c in directions:
                nr,nc = row+r,col+c

                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    continue
                
                if matrix[nr][nc] > matrix[row][col]:
                    max_path_dfs = max(max_path_dfs,1 + dfs(nr,nc))
            
            dp[row][col] = max_path_dfs
            return dp[row][col]
              
        max_path = 0
        for i in range(ROW):
            for j in range(COL):
                max_path = max(max_path,dfs(i,j))
        
        return max_path       

if __name__ == "__main__":
    s = Solution()
    print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    print(s.longestIncreasingPath([[1]]))