# https://neetcode.io/solutions/redundant-connection
# Here cycle detection in indirected graph won't work because of graph with cycle like this 1 -> 2 -> 3 -> 4 -> 5 -> 3
# Here loop happens bw 5 and 3. but my algo will check for index in the whole array when we should only check bw 3 and 5 nodes

# But you can solve this problem with dfs cycle detection, make adj_list as you run dfs, if for a edge loop is detected, return that edge

# Use disjoint set union here, make connections one by one, if a connection returns 0 then, loop will form there because n1 and n2 have same root parent[THINK]
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(0,n+1)]
        rank = [1 for _ in range(0,n+1)]

        def find(n):
            res = n
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        for u, v in edges:
            if union(u,v) == 0:
                return [u,v]
                
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))    
        

        


        
