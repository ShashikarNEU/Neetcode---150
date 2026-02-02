from collections import defaultdict
from typing import List


# Optimal way(Logic)
# Have a isReachable n*n matrix
# do DFS on every course, and mark (current_course, i) (isReachable[parent][source] = True) in every step via BFS/DFS
# iterate queries and check isReachable

# TC = O(n*(V+E)), SC = O(V+E)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        isReachable = [[False]*n for i in range(n)]
        adj_list = defaultdict(list)
        for u,v in prerequisites:
            adj_list[u].append(v)

        def dfs(source, parent, visited):
            if source in visited:
                return
            
            visited.add(source)
            isReachable[parent][source] = True
            
            if source in adj_list:
                nodes = adj_list[source]
                for node in nodes:
                    dfs(node, parent, visited)
        
        visited = set()
        for i in range(n):
            dfs(i,i,visited)
            visited = set()
        
        res = []
        for u,v in queries:
            res.append(isReachable[u][v])
        
        return res
            
            
            