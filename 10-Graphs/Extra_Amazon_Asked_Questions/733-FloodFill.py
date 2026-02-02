# Matrix BFS
from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROW = len(image)
        COL = len(image[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        visited = set()

        q = deque()
        q.append((sr,sc))
        visited.add((sr,sc))
        starting_pixel_color = image[sr][sc]
        image[sr][sc] = color

        while q:
            row, col = q.popleft()

            for r,c in directions:
                nr, nc = row+r, col+c

                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or (nr,nc) in visited or image[nr][nc] != starting_pixel_color:
                    continue
                
                image[nr][nc] = color
                visited.add((nr,nc))
                q.append((nr,nc))
        
        return image

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

