# Here do BFS not DFS
# BFS is for shortest path/route and DFS for longest path

# For this question, since we need shortest from 0 to every node. Do BFS
# Reverse the question and start from 0's and not other index. it's easier that way
# For BFS, in queue instead of having a other varible incrementing path, you can just append(row, col, path+1)
# pop it and then assign min of grid[r][c] and path.

# One BFS Run (Multiple times)
# TC = O((m*n)*(no of gates))
# SC = O(m*n)
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        
        def bfs(r, c):
            queue = deque()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            path = 0
            visited = set()
            queue.append((r,c,0))
        
            while queue:
                r, c, path = queue.popleft()
                grid[r][c] = min(path, grid[r][c])

                for row,col in directions:
                    if r + row < 0 or c + col < 0 or r + row >= ROW or c + col >= COL or grid[r+row][c+col] == -1:
                        continue
                    if (r+row, c+col) not in visited:
                        queue.append((r+row, c+col, path+1))
                        visited.add((r+row, c+col))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    bfs(r, c)

# Optimal soln
# Multi-Source BFS
# we push all the gates into the queue and do BFS
# we have a visited set here.
# if a gate reaches a cell before other gate can reach then it's the shortest distance. so, having a visited array won't cause any harm[IMP]
# Remember, always put it in visited array and then start bfs
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW = len(rooms)
        COL = len(rooms[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()
        visited = set()
        # Putting all gates into the queue
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))

        while q:
            row, col, dist = q.popleft()

            rooms[row][col] = dist

            for r,c in directions:
                nr, nc = row+r, col+c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or rooms[nr][nc] == -1 or (nr,nc) in visited:
                    continue
                visited.add((nr,nc))
                q.append((nr,nc,dist+1))

# Other attempt
# Enque all sources then append None into the queue. When none appears increment dist and assign it during BFS. Kind of like a lv order(levels). Have a visited arr also. if the source reaches a point then that's the min distance.
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW = len(rooms)
        COL = len(rooms[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        queue = deque()
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        queue.append(None)
        dist = 0
        visited = set()

        while queue:
            node = queue.popleft()

            if node == None:
                if queue:
                    dist+=1
                    queue.append(None)
            else:
                row, col = node[0], node[1]

                rooms[row][col] = dist

                for r,c in directions:
                    nr, nc = row+r, col+c
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or rooms[nr][nc] == -1 or (nr,nc) in visited:
                        continue
                    
                    queue.append((nr,nc))
                    visited.add((nr,nc))

                
# Call the test function
if __name__ == "__main__":
    s= Solution()
    grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    s.islandsAndTreasure(grid)
    print(grid)
    grid2 = [[2147483647,2147483647,2147483647],[2147483647,-1,2147483647],[0,2147483647,2147483647]]
    s.islandsAndTreasure(grid2)
    print(grid2)
      


