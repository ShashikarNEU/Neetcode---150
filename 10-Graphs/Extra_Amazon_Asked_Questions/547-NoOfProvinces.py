class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
        
        parent = [i for i in range(n)] # index -> node, value -> parent
        rank = [0]*n

        def find(n):
            res = n
            while parent[res] != res:
                parent[res] = parent[parent[res]] # Path decompression
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            # loop exists
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        num = n
        for u,v in edges:
            num-=union(u,v)
        
        return num
        
