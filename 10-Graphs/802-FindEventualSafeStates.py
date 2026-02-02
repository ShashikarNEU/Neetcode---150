from collections import defaultdict, deque
from typing import List

# Observe the question
# Try kahn's algo after reversing the edges
# You can solve this with DFS + Coloring also

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        n = len(graph)
        adj_list = defaultdict(list)
        indegree = [0]*n

        for i,nodes in enumerate(graph):
            for node in nodes:
                adj_list[node].append(i)
                indegree[i]+=1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        
        while queue:
            node = queue.popleft()
            nodes = adj_list[node]
            for neighbours in nodes:
                indegree[neighbours]-=1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
            adj_list[node] = []
            res.append(node)
        
        res.sort()
        return res



        
        
        




        