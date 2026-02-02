# perform dfs in the matrix only, don't convert to dict.
# matrix dfs is given below
# make visted indexes 0 instead of using a visited set. You have 4 directions to go.(top,bottom,right,left)
# there are restriction codn. if row<0 or col <0 or grid[i][j]=0 or row>=len(grid) or col >= len(grid[0]) then return
# if it does not return, make grid[i][j] = 0 to mark it as visited. Check the no of dfs runs to find the no of islands

class Solution:           
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        self.directions = [[0,1],[1,0],[-1,0],[0,-1]] # Top,Right,Bottom,Left
        self.ROW = len(grid)
        self.COL = len(grid[0])

        def dfs(rows, col):
            if (rows >= self.ROW or col >= self.COL or grid[rows][col] == "0" or rows < 0 or col < 0):
                return
            
            grid[rows][col] = "0"

            for r,c in self.directions:
                dfs(rows + r, col + c)
        
        for r in range(self.ROW):
            for c in range(self.COL):
                if grid[r][c] != "0":
                    islands+=1
                    dfs(r,c)
        
        return islands

# Test Case
if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    s = Solution()
    
    print(s.numIslands(grid)) # Expected output: 3