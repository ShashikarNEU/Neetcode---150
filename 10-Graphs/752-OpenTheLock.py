from collections import deque
from typing import List

# Logic
# Hint :- We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`

# Use BFS starting with 0,0,0,0
# Now, lock turn logic will be a issue here
# 8 turns are possible - one forward for each lock and one backward for each lock
# directions = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]
# 0-> 9 and 9->0 turn logic is imp
# for forward, (d+1)%10 is enough for 0->9 and going back 0 from 9
# [TRICKY]for backward, (d-1+10)%10 is required, think of edge case like 0-1+10 % 10 or normal case of going from 5->4
# Have dist as an argumant in the node in the node
# Rest of question is easy
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append((0,0,0,0, 0)) # four locks and distance
        directions = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]
        deadends = set(deadends)
        dist = 0
        visited = set()
        
        while queue:
            l1, l2, l3, l4, dist = queue.popleft()

            res_str = ""
            res_str += str(l1)
            res_str += str(l2)
            res_str += str(l3)
            res_str += str(l4)
            
            if res_str in deadends:
                continue

            if res_str == target:
                return dist

            for a,b,c,d in directions:
                na, nb, nc, nd = 0,0,0,0
                if a < 0 or b < 0 or c < 0 or d < 0:
                    na, nb, nc, nd = (l1+a+10)%10, (l2+b+10)%10, (l3+c+10)%10, (l4+d+10)%10
                else:
                    na, nb, nc, nd = (l1+a)%10, (l2+b)%10, (l3+c)%10, (l4+d)%10
                
                if (na, nb, nc, nd) not in visited:
                    queue.append((na,nb,nc,nd,dist+1))
                    visited.add((na,nb,nc,nd))
        
        return -1
                
                




                







