# Multi-Source BFS
# Refer Rotting oranges and (wall and gates) problems for reference

from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ROW = len(mat)
        COL = len(mat[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()
        visited = set()
        # Putting all 0's into the queue
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))

        while q:
            row, col, dist = q.popleft()

            mat[row][col] = dist

            for r,c in directions:
                nr, nc = row+r, col+c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or (nr,nc) in visited:
                    continue
                visited.add((nr,nc))
                q.append((nr,nc,dist+1))
        return mat