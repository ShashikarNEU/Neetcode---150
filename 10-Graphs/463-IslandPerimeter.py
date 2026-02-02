from typing import List

# Logic:- no DFS or BFS required
# just use count the squares by perimeter(+ 4 everytime)
# and if the squares clash top or left side, do area -=2 to subtract overlapping sides
# return area
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[-1,0],[0,-1]]
        area = 0
        #visited = set()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    area += 4
                    #visited.add((row,col))
                
                    for r,c in directions:
                        nr, nc = row+r, col+c
                        if nr < 0 or nc < 0:
                            continue
                        if grid[nr][nc] == 1:
                            area -= 2
        
        return area
                    




        
        