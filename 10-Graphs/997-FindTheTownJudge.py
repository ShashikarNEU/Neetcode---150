from typing import List

# Think of topo sort & kahn's algo
# but that's overkill
# we need to check for indegree 0 and to see judge is connected to everything else
# have a indegree and outdegree array
# check if indegree = 0 and outdegree = n-1 return that vertex
# TC = O(v+e), SC = O(V)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0]*(n+1)
        outDegree = [0]*(n+1)

        for u,v in trust:
            inDegree[u]+=1
            outDegree[v]+=1
        
        for i in range(1,n+1):
            if inDegree[i] == 0 and outDegree[i] == n-1:
                return i
        
        return -1

        
