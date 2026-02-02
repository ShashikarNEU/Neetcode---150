# Use Multi-Source BFS here
# Put all rotten oranges into queue first, pop them out, check in all directions and enqueue them
# when enqueing, make them rotten. In BFS, if any place = 0 or 2, return/skip it. out of range directions -> skip it
# For minute tracking, all items in the queue have to be checked so, for that append None after rotten oranges in the start. if none is popped then, 1 minute has passed(All current queue items are done) -> insert None if queue not empty or use for loop for all items in queue(Neetcode way)
# if any 1s remianing return -1
# [IMP] for first None popped, minute will pass also(1 extra minute) so, pass minute as -1 in the start or return minute - 1 as the answer

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        minutes = 0
        queue = deque()
        
        fresh_oranges = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        queue.append(None)

        while queue:
            node = queue.popleft()

            if not node:
                if queue:
                    minutes+=1
                    queue.append(None)
            else:
                row, col = node[0], node[1]

                for r,c in directions:
                    nr, nc = row+r, col+c

                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr,nc))
        
        return minutes if fresh_oranges == 0 else -1

# Other Attempt(Did for loop inside for minute tracking)
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                    
        
        minute = -1
        
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                for r,c in directions:
                    nr, nc = row+r, col+c
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            minute+=1
       
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        
        return minute if minute != -1 else 0

# Call the test function
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: Simple case, all oranges rot in 1 minute
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print(solution.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))  # Minimum time required: 4 minutes

    # Test Case 2: All oranges are already rotten
    grid2 = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
    print(solution.orangesRotting(grid2))  # No time needed

    # Test Case 3: Impossible case, fresh orange is isolated
    grid3 = [
        [0]
    ]
    print(solution.orangesRotting(grid3))  # Fresh orange can't be reached

    # Test Case 4: No oranges in the grid
    grid4 = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(solution.orangesRotting(grid4)) # No time needed

    # Test Case 5: Single fresh orange with no rotten ones
    grid5 = [
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(solution.orangesRotting(grid5))  # No rotten orange to start with

    # Test Case 6: Large grid with spreading infection
    grid6 = [
        [2, 1, 0, 2, 1],
        [1, 1, 1, 1, 0],
        [0, 1, 2, 1, 1],
        [1, 0, 1, 2, 1]
    ]
    print(solution.orangesRotting(grid6))  # Minimum time required: -1

    print("All test cases passed!")
            

        