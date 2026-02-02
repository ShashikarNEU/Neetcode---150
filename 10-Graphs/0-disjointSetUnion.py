# Disjoint Set Union (DSU) / Union-Find Algorithm - https://www.youtube.com/watch?v=8f1XPm4WOUc&t=941s [WATCH THIS FIRST!!]

# 1. Initialization:
#    - Create a 'parent' array where each node is its own parent initially (parent[i] = i).[Index are the nodes, the values are the parent]
#    - Create a 'rank' (or 'size') array to keep track of tree depth or size. The rank is 1 for everything in the start

# 2. Find Operation (Path Compression):
#    - To find the representative (root) of a node x, move up the parent chain until reaching the root.
#    - Apply "path compression" by directly linking all visited nodes to the root, making future lookups faster.

# 3. Union Operation (Union by Rank/Size):
#    - Find the roots of both sets using the 'find' function.
#    - If roots are different:
#      - Attach the smaller tree under the larger tree (union by rank/size) to keep the structure balanced.
#      - Update the 'parent' and, if using rank, update the rank of the new root.

# 4. Time Complexity:
#    - Find and Union operations are nearly constant time O(α(n)),
#      where α(n) is the inverse Ackermann function (very slow-growing, almost constant in practical cases).

# 5. Applications:
#    - Connected Components in a Graph
#    - Kruskal’s Algorithm for Minimum Spanning Tree
#    - Cycle Detection in an Undirected Graph
#    - Network Connectivity Problems

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
            
            



        
            
