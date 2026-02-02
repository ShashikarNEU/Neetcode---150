# https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32
## Djikstra's Algorithm using adjacency list and min heap

# Weighted directed graph is given to you and you need to find the min distance from the source node to all nodes

# In djikstra's algo, you use BFS + min heap(Priorty Queue) since there are multiple weight edges bw the same two nodes. you take all those edges in a min heap, pop the min weight/distance, insert it into the result dict. result dict also acts as a visited set, you do not search for neighbours if node already in result dict(this means it is a same edge with diff weight)

# Refer this graph in 0-djiktra-example.py

# Directed Graph
adj_list = {
    1: [(2, 1), (4, 4)],
    2: [(5, 10), (3, 1)],
    3: [(4, 1)],
    4: [],
    5: [(4, 4)]
}

# Undirected graph
adj_list1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# You can be given a edge list also here so be prepared - so make a adjacency list from that

import heapq
def djikstra_algo(source, adj_list):
  min_heap = []
  heapq.heappush(min_heap, (0, source))
  distance_dict = {}

  while min_heap:
    distance_prev, node = heapq.heappop(min_heap)

    # if node is in distance_dict, it already has the smallest weight/distance cuz of min heap updating it with longer distance/weight is waste
    if node not in distance_dict:
      distance_dict[node] = distance_prev

      if node in adj_list:
        nodes = adj_list[node]
        for node, distance in nodes:
          heapq.heappush(min_heap, (distance + distance_prev, node))
  
  return distance_dict

# Use visited set instead of using distance dict as visited set
import heapq
def djikstra_algo2(source, adj_list):
  min_heap = []
  heapq.heappush(min_heap, (0, source))
  distance_dict = {}
  visited = set()

  while min_heap:
    distance_prev, node = heapq.heappop(min_heap)
    # Visited logic
    if node in visited:
      continue
    visited.add(node)

    distance_dict[node] = distance_prev

    if node in adj_list:
      nodes = adj_list[node]
      for node, distance in nodes:
        heapq.heappush(min_heap, (distance + distance_prev, node))
  
  return distance_dict

print(djikstra_algo(1, adj_list)) # Directed graph
print(djikstra_algo('A', adj_list1)) # Undirected graph

print(djikstra_algo2(1, adj_list)) # Directed graph
print(djikstra_algo2('A', adj_list1)) # Undirected graph

# Djikstra won't work in case of negative weights, or negative cycles
# We can transverse back to forth and keep descreasing the distance since distance is negative but algo will take only the first value
# since it's coming from min heap

# TC = (E+V) * log(V) (E - Edges, V - Vertex)

# Dijkstra Variants :
# Both versions are correct - One uses visited set. Other uses distance array and checks if shorter distance found
# 1. This version uses a visited set — no need for `if new_dist < dist[node]` check.
#    - We only process each node the first time it's popped from the heap,
#      which is guaranteed to be the shortest path due to min-heap ordering.
# 2. Alternative "relaxation-style" Dijkstra:
#    - Uses distance[] array and updates distances if a shorter path is found.
#    - Requires: `if dist[u] + weight < dist[v]:` before updating.
#    - Does not use a visited set — nodes may be pushed into the heap multiple times.

# Print shortest path for djikstra's algo given the dest and source
# Do Normal djikstra like usual but have a shortest path parent array, every time you find a shortest path to node, store its parent
# Tranverse the parent array from back for ths answer
def djikstra_path(source, dest, adj_list, n):
  min_heap = []
  visited = set()
  min_heap.append((0, source, None)) # weight, starting node, parent
  shortest_path = [0] * n

  while min_heap:
    weight_prev, node, parent = heapq.heappop(min_heap)
    if node in visited:
      continue
    visited.add(node)
    # Update shortest path for that node
    shortest_path[node] = parent if parent else 0
    if node == dest:
      break
    neighbours = adj_list[node]
    for neighbour, weight in neighbours:
      heapq.heappush(min_heap, (weight_prev + weight, neighbour, node))
  
  result = [dest]
  res = dest
  while shortest_path[res] != source:
    result.append(shortest_path[res])
    res = shortest_path[res]
  result.append(source)
  return result[::-1]

graph = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}

print(djikstra_path(0, 3, graph, 4))




