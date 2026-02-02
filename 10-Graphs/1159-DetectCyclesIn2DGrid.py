from typing import List

# Key Point:- this is undirected but DFS cycle detection is for directed(topo sort)
# so you have to change it a little
# you need to track prev and not visit the parent in the directions loop
# if (nr,nc) == prev: continue
# if you find the cycle, rest of the code is easy

# we should not visit the grid value where we already traversed so, add if it's not in visited set
# Have a global visited set to reduce the work
# Think Why!(You should not do DFS on the same loop/not loop again)
                    
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        def dfs(row, col, target, prev):
            if (row, col) in visited:
                return True
                  
            visited.add((row,col))

            for r,c in directions:
                nr, nc = row+r, col+c

                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    continue
                
                # Very Imp(you write this here not above in recursion)
                if (nr,nc) == prev:
                    continue
                
                if grid[nr][nc] == target:
                    if dfs(nr, nc, target, (row,col)):
                        return True
            
            return False
        
        for i in range(ROW):
            for j in range(COL):
                if (i, j) not in visited and dfs(i,j, grid[i][j], (-1,-1)):
                    return True
        
        return False




        

        