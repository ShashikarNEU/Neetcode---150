# Simple logic -> convert to adj list and run DFS for every node(with visited set) to find the no of connected components
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = {}

        # Converting the input to adj list
        for u,v in edges:
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append(v)

            if v not in adj_list:
                adj_list[v] = []
            adj_list[v].append(u)

        visited = set()

        def dfs(source):
            if source in adj_list:
                nodes = adj_list[source]
                for node in nodes:
                    if node not in visited:
                        visited.add(node)
                        dfs(node)
        
        connected_components = 0
        for node in range(n):
            if node not in visited:
                connected_components += 1
                dfs(node)
        
        return connected_components
    
# Using Union Find(Disjoint Set Union)
class Solution:    
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)] # Every node's parent is itself

        rank = [1]*n # Every node has size(rank) 1 in the start

        def find(n):
            res = n
            while parent[res] != res:
                parent[res] = parent[parent[res]] # Path decompression(You are setting grandparents value to the node - reducing the path)
                res = parent[res] # Updating the value of res, jumping through parent arr to find the root
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0 # Already connected
            
            # Given two nodes, find their parents, if not same, compare the rank, connect them
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
              
            return 1
        
        connected_components = n 
        for u,v in edges:
            result = union(u, v)
            connected_components -= result
            
        return connected_components
            
            
                    
                

        