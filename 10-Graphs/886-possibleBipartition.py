# https://www.youtube.com/watch?v=mev55LTubBY -> Watch this for algo
# Use BFS to get all the neighbours, mark them as -1. Have a visited array as color list, 1 for red, -1 blue and 0 for invisited
# mark souirce as 1 in the beginning and do bfs, bfs will automatically mark everything with color but if it encounters a node with 
# the same color as itself, that means there is a loop(we need 3 colors, not bipartited), return False. if color[node] == 0 not visited

# dislikes array means that a,b both a and b don't like each other(indirected graph)

# when dislikes array makes edges, no nodes connected can be in the same set so, this problem is a 2-color problem

# in BFS, we can recive opp color colors, but if we recieve the same color, we return False
# Carry color into the queue -> (node, color)
# colorArr = [0]*(n+1), treat 0 as unvisited

# LinkedLn follow up:- what about n colors? or 3 colors?

from collections import defaultdict, deque
from typing import List
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        queue = deque()
        colorArr = [0]*(n+1)
        adj_list = defaultdict(list)

        # Undirected graph
        for u,v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Reason for writing a fn here is beacuse of disconnected components
        def bfs(start):
            queue.append((start, 1))
            colorArr[start] = 1

            while queue:
                node, color = queue.popleft()

                if node in adj_list:
                    nodes = adj_list[node]
                    for neighbours in nodes:
                        if colorArr[neighbours] == 0:
                            colorArr[neighbours] = -1 * color
                            queue.append((neighbours, -1 * color))
                        elif colorArr[neighbours] == color:
                            return False
            
            return True
        
        for i in range(1,n+1):
            if colorArr[i] == 0:
                if not bfs(i):
                    return False
        
        return True

# n color problem
# Use DFS + Backtrack
# Since we can't determine the color greedily, we must try a color,
# move to the next node, and if we get stuck, undo that choice (backtrack) 
# and try a different color.
class Solution:
    def graph3Coloring(self, n: int, graph: List[List[int]]) -> bool:
        colors = [0] * (n + 1)  # 0: Uncolored, 1, 2, 3: Colors

        def can_color(node, c):
            # Check if any neighbor has this color 'c'
            for neighbor in graph[node]:
                if colors[neighbor] == c:
                    return False
            return True

        def backtrack(node):
            if node > n:  # All nodes colored successfully
                return True
            
            # Try all 3 colors for the current node
            for c in range(1, 4): 
                if can_color(node, c):
                    colors[node] = c  # Assign color
                    if backtrack(node + 1):  # Move to next node
                        return True
                    colors[node] = 0  # Backtrack (undo)
            
            return False # No color worked for this node

        return backtrack(1)




                                
                        

            


