# Check inDegree of every node and form a array
# Form a adj list, but in a opp directions -> First course should have 0 inDegree 
# So, acc to that, make a adj_list
# Push all in degree's with 0 to a queue
# when you pop from the queue, remove all it's edges, decrement indegrees for the affected
# add the popped source to result
# but if indegree when decrementing, add it to the queue

# Visualizing the algo with example is easier, refer algo video also
# Video -> https://www.youtube.com/watch?v=73sneFXuTEg

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Kahn's Algo
        adj_list = defaultdict(list)
        inDegree = [0]*numCourses
        queue = deque()
        res = []

        for u,v in prerequisites:
            adj_list[v].append(u)
            inDegree[u]+=1
        
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            source = queue.popleft()
            nodes = adj_list[source]
            for node in nodes:
                inDegree[node]-=1
                if inDegree[node] == 0:
                    queue.append(node)
            adj_list[source] = []
            res.append(source)
        
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(2, [[0,1]]))
    

        