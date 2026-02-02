from collections import deque
from typing import List

# Logic
# Use DFS and mark the first island with 2
# Then do BFS with all island 1 nodes in the queue
# Don't mistake this as multi-source BFS, We can process in any order 
# but the smaller distance will always reach island 2 first

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] != 1:
                return
            
            grid[row][col] = 2

            for r,c in directions:
                nr,nc = row+r,col+c
                dfs(nr,nc)
        
        # Mark the first island with 2's with a DFS
        found = False
        for i in range(ROW):
            if found:
                break
            for j in range(COL):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
        
        # Multi Source BFS
        q = deque()
        visited_bfs = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited_bfs.add((i,j))  # Add starting cells to visited!
        
        while q:
            node = q.popleft()
            row, col, distance = node[0],node[1],node[2]

            for r,c in directions:
                nr,nc = row+r,col+c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    continue
                if (nr,nc) in visited_bfs:
                    continue
                if grid[nr][nc] == 1:  # Reached second island
                    return distance
                visited_bfs.add((nr,nc))
                q.append((nr,nc,distance+1))
        
        return -1