# https://neetcode.io/solutions/reconstruct-itinerary
# Step 1 -> sort it for small lexigraphic order, then form the adj list(Alternatively, you can sort adj[keys] after forming adj list)
# Step 2 -> Do DFS but instead of keeping a visited set, you can use remove the edge in adj list after traversing it
# Step 3 -> Edge Case, if you go to a small lex edge and that edge has no returning edges then, you need to back track(Which makes the order wrong) since you have to follow a single path. In that case, you will need to choose the other edge even tho it has large lex value. In that case, you have to add the edge back in that position, remove the node from result after recursion call. 
# When result length is length of tickets + 1, algo is over.

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj_list = {}
        tickets.sort()
        for u, v in tickets:
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append(v)
        
        #adj_list = {u: sorted(adj_list[u]) for u in adj_list}

        # Other Way to Sort
        # for u in adj_list:
        #   adj_list[u].sort()
        
        #print(adj_list)
        
        result = ["JFK"]
        def dfs(source):
            if len(result) == len(tickets) + 1:
                return True
            # Edge case
            if source not in adj_list:
                return False
            
            #temp = list(adj_list[source])
            for index, node in enumerate(adj_list[source]):
                adj_list[source].pop(index)
                result.append(node)

                if dfs(node):
                    return True
                
                # if returned False
                adj_list[source].insert(index, node)
                result.pop()
            return False
        
        dfs("JFK")
        return result

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]
        
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
