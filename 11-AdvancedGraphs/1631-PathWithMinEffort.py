# This is a variation of Djikstra's algo/Prim algo's, almost everything is same with one slight change
# Djikstra algo will find every path with minimized weight (also has visited logic)
# so, for every path, track max diff in that path and put it into a min heap

# LinkedIn OA Question 2 (Same question worded differently but I need to track max distance/weight instead of diff bw distances/weights while finding min/shortest path) but path length k is already given (consider all paths <=k)
import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        ROW = len(heights)
        COL = len(heights[0])
        visited = set()
        min_heap = []
        min_heap.append((0,0,0)) # (Difference, r, c)

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_diff = 0

        while min_heap:
            difference, r, c = heapq.heappop(min_heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            print((difference, r, c))
            if r == ROW - 1 and c == COL - 1:
                return difference
            for row, col in directions:
                new_r , new_c = r + row, c + col
                if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL:
                    continue
                max_diff = max(difference, abs(heights[new_r][new_c] - heights[r][c]))
                heapq.heappush(min_heap, (max_diff, new_r, new_c))

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
    print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
    print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
  
    
                    

