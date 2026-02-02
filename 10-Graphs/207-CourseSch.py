# Cource Sch 1/2 will work in directed cycle detection, not undirected cycle detection. For undirected cycle detection, pls check leetcode -261(Graph valid tree)
# Reason, undirected has a loop bw one edge A->B means B->A so, loop prrsent -> False which is wrong so, we need a other algo for that.

# https://neetcode.io/solutions/course-schedule
# Watch video first!!
# Use DFS here but bit differently
# Use visiting here and after every recursion stack, when going back remove that node from adj[source]
# One by one, remove all neighbours when going back in the adj list. Once all neighbours nodes have been 
# visited, pop node from visting since only the current path is there in visiting
# When going back in recursion, remove that value from adj_list.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses
        # Creating adj list
        adj_list = [[] for i in range(n)]
        for u,v in prerequisites:
            adj_list[u].append(v)
        
        visiting = set()

        def dfs(source):
            if source in visiting:
                return False
            if len(adj_list[source]) == 0:
                return True
            
            visiting.add(source)
            
            nodes = adj_list[source]
            for node in nodes:
                if not dfs(node):
                    return False
                #adj_list[source].remove(node) # my logic - it works!!
            visiting.remove(source)
            adj_list[source] = [] # Removing every neighbour node after visiting everything
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True

# Can course sch 2 algo for course sch 1 also, only key change is that -> instead of removing all edges after fully visiting fanouts of a node, we are adding it in visited set.instead of adj_list[source] = [], we are checking in visited now. They mean the same thing
# We can use both in case of toplogical sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # I am using a list instead of dict but can use dict also here
        adj_list = [[] for i in range(numCourses)]
        # adj_list = defaultdict(list)

        for u,v in prerequisites:
            adj_list[u].append(v)

        cycle = set()
        visited = set()
        course_order = []
        
        def dfs(source):
            if source in cycle:
                return False
            
            if source in visited:
                return True
            
            cycle.add(source)

            nodes = adj_list[source]
            for node in nodes:
                if not dfs(node):
                    return False
                #adj_list[source].remove(node)
            #adj_list[source] = []
            cycle.remove(source)
            visited.add(source)
            course_order.append(source)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        
