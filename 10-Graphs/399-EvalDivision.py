from collections import defaultdict, deque
from typing import List

# Logic
# Think about this - (a/c)*(c/b) == (a/b)
# This is like a path from a to b via c
# Now, imagine a path going through 10 nodes from a to c(everything gets cancelled out in between)
# We can BFS or DFS but BFS is easier
# Define a BFS function. have queue, visited declared inside fn since it's not recursive
# for making adj_list, use Zip and think about the logic


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for (u,v) , w in zip(equations, values):
            adj_list[u].append((v,w))
            adj_list[v].append((u,(1/w)))
        
        def bfs(source, target):
            queue = deque()
            queue.append((source,1))
            visited = set()
            visited.add(source)

            while queue:
                node, weight = queue.popleft()

                if node not in adj_list or target not in adj_list:
                    return -1

                if node == target:
                    return weight
                
                nodes = adj_list[node]
                for neighbours, w in nodes:
                    if neighbours not in visited:
                        visited.add(neighbours)
                        queue.append((neighbours, weight*w))
            
            return -1
        
        res_arr = []
        for source, target in queries:
            res = bfs(source, target)
            res_arr.append(res)
        
        return res_arr


        
        

        