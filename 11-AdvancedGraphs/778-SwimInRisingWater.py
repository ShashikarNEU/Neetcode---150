# Question is complex but soln is straight forward. Look at the two test cases in leetcode
# Just look at the second exmaple pls(it's screaming djistra)
# Notice something?
# grid values are weight and path is always the min path taken
# Use Djikstra
import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        min_heap = [(grid[0][0],0,0)] # (water lv, row, col)
        visited = set() # Should have (r,c)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        max_water_lv = grid[0][0]

        while min_heap:
            water_lv, row, col = heapq.heappop(min_heap)

            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            #print((row, col))
            max_water_lv = max(water_lv, max_water_lv)

            if row == ROW - 1 and col == COL - 1:
                return max_water_lv

            for r,c in directions:
                new_row, new_col = row + r, col + c
                if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL:
                    continue
                heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))
        
        return max_water_lv

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.swimInWater([[0,2],[1,3]]))
    print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))



