# https://neetcode.io/solutions/min-cost-to-connect-all-points
# Prim algo is used to find the min spanning tree out of graph. if there is a graph with > n edges with weights.
# this algo will return the Min Spanning Tree with n-1 edges with the min weight. it will connect all nodes to each other with min
# cost edges, so that the grpah is connected and becomes a tree(n-1 edges)

# [Varition of djikstra's algo - Very Similar]
# Definition of Prim's Algorithm:
# Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph.
# An MST connects all the vertices with the minimum possible total edge weight, and without any cycles.

# Key Idea:
# Start from any node, and repeatedly add the smallest-weight edge that connects a vertex in the MST to a vertex outside the MST, until all nodes are included.

# 🪜 Step-by-Step:
# Choose any starting vertex.
# Mark it as part of the MST.
# Add all edges from the current MST to a priority queue (min-heap) based on weight.

# Pick the smallest edge that connects to a vertex not yet in the MST.

# Repeat until all vertices are in the MST.

# ⏱️ Time Complexity:
# Using a min-heap + adjacency list:
# O(E log V) where
# E = number of edges
# V = number of vertices
import heapq
def prim_algo(adj_list):
  min_heap = []
  min_heap.append((0, 0)) # (distance, starting node)
  visited = set()
  min_cost = 0 # min cost to create the spanning tree

  while min_heap:
    weight_prev, node = heapq.heappop(min_heap)

    if node in visited:
      continue

    visited.add(node)
    print(weight_prev, node)
    min_cost += weight_prev
    
    neighours = adj_list[node]
    for neighbour, weight in neighours:
      heapq.heappush(min_heap, (weight, neighbour))
    
  return min_cost

# Refer to Prim graph example png for the graph
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6),
    (3, 5, 5),
    (1, 5, 10),
    (0, 4, 7)
]

# Making a adj list out of the edge list
adj_list = [[] for _ in range(0,6)]
for u, v, weight in edges:
  adj_list[u].append((v, weight))

print(adj_list)
print(prim_algo(adj_list))




