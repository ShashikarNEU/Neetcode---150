# https://neetcode.io/solutions/pacific-atlantic-water-flow
# Brute Force Soln
# I did DFS for every node following the contraints and checked if it reached the pacific and altantic ocean, if it reached both ocean
# Add it to the result array and return it
# but it is not optimal as, we are running dfs for every node and clearing the visited set after each run
# Time - 4^n
class Solution:
    def pacificAtlanticBrute(self, heights: list[list[int]]) -> list[list[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, pacific, altantic):
            if (r,c) in visited:
                return
            
            if r < 0 or c < 0:
                pacific[0] = True
                return
            if r >= ROW or c >= COL:
                altantic[0] = True
                return
            
            visited.add((r,c))

            for row, col in directions:
                if r+row >= 0 and c+col >= 0 and r+row < ROW and c+col < COL:
                    if heights[r][c] < heights[r+row][c+col]:
                        continue
                dfs(r + row, c + col, pacific, altantic)
        
        result = []
        pacific = [False]
        altantic = [False]
        for r in range(ROW):
          for c in range(COL):
              dfs(r, c, pacific, altantic)
              if pacific[0] and altantic[0]:
                  result.append([r,c])
              pacific[0] = False
              altantic[0] = False
              visited.clear()
        
        return result

# For optimal soln, we reverse the problem, run dfs from the oceans to the nodes along the boundaries
# reverse the codn for flow of water. Have two visited sets - pacific and altantic for both boundaries. After running dfs along
# the boundaries, take common ans in pacific and atlantic sets, add them to result and return it
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col, ocean, visited):
            if (row, col) in visited:
                return
            
            visited.add((row,col))
            ocean.append((row,col))

            for r,c in directions:
                nr, nc = row+r, col+c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    continue
                if heights[row][col] > heights[nr][nc]:
                    continue
                dfs(nr,nc,ocean,visited)
        
        atlantic = []
        pacific = []
        visited_pacific = set()
        visited_atlantic = set()

        for c in range(COL):
            dfs(0, c, pacific, visited_pacific)
            dfs(ROW-1, c, atlantic, visited_atlantic)
        
        for r in range(ROW):
            dfs(r, 0, pacific, visited_pacific)
            dfs(r, COL-1, atlantic, visited_atlantic)
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        
        return res
    
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
                  

                


            
