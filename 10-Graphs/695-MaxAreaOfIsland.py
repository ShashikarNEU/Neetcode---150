# FOLLOW UP TO NO OF ISLANDS - 200
# Use maxArea to find the area
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        max_area = 0
        area = [0] # Storing in recursion using pass by value(Array stores value after the func call)/ you can use nonlocal area also
        
        def dfs(r,c, area):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return
            
            area[0] += 1
            grid[r][c] = 0 # mark it as visited

            for row,col in directions:
                dfs(r + row, c + col, area)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] != 0:
                    dfs(r,c,area)
                    max_area = max(area[0], max_area)
                    area[0] = 0
                    
        return max_area

# When we visit the island, area is 1 then we count neighbours/or go down(bfs/dfs)
# Interviewers will except this rather than the previous solution
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            for r,c in directions:
                area += dfs(row+r,col+c)
            return area
            
        maxArea = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea
        
# Test Case
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    s = Solution()
    
    print(s.maxAreaOfIsland(grid)) # Expected output: 4

