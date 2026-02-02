# Valid Tree means 2 conditions - has no loop and is not disconnected
# For loop detection, algo is almost same as course sch 1/2 with slight change. 
# Track the parent of the node and in next recusion, don't
# go back to the parent again(def dfs(source, parent)) for neighbours in source-> parent != neighbours
# Means -> 1 <-> 2 but don't go back to 1 again while checking for loop

# OR you can use disjoint set union here. When the union returns 0, return False(Loop is formed)

# DFS cycle detection method
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj_list = [[] for i in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        cycle = set()
        visited = set()

        def dfs(source, parent):
            if source in visited:
                return True
            if source in cycle:
                return False
            #print(source)
            cycle.add(source)
            nodes = adj_list[source]
            for node in nodes:
                if parent != node:
                    if not dfs(node, source):
                      return False
            cycle.remove(source)
            visited.add(source)
            return True
        
        # Cycle detection
        if not dfs(0, None):
            return False
        print(visited)
        # If the full tree is connected or not
        if len(visited) < n:
            return False
        return True

# Disjoint set union method
# Check for loop (union is not possible)
# Check if connected componenets is 1 or more than 1.
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # check for a cycle
        # check if it's connected
        # DSU
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        connected_componenets = n
        for u,v in edges:
            res = union(u, v)
            if res == 0:
                return False
            connected_componenets -= res
        
        return True if connected_componenets == 1 else False

# TC = O(V+(E*amor(V))), SC = O(V)

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

                


            
            