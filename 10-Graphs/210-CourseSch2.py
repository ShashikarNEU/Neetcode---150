# For top sort, don't use visited as answer. Always have a result list for ans[IMP]
# Reason: Set won't have order, list will have order
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # I am using a list instead of dict but can use dict also here
        adj_list = [[] for i in range(numCourses)]

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
                #adj_list[source].remove(node) # course sch 1
            #adj_list[source] = [] # course sch 1
            cycle.remove(source)
            visited.add(source)
            course_order.append(source)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return course_order

if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(2, [[0,1]]))
    

        