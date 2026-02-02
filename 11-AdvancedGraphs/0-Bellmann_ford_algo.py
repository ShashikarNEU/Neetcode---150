# https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=41 [Good video for concept]
# Bellmann ford only takes directed edge list as input
# it is used to check for shorter distances like djikstra but it can handle negative weights and negative cycles
# Initially, we have the dist array with float('inf') for every node
# when we traverse the edge list, (source, dest, weight) -> we check for dist[source] + weight < dist[dest] 
# if yes, update dist[dest]. We do this n-1 times to get all the nodes updated with the shortest path from source
# Bellmann ford takes n-1 iterations for the all nodes shortest paths to get computed.

# Bellman-Ford Algorithm:
# - Handles negative weights
# - Relax all edges (n - 1) times
# - 1 extra pass: if any edge (u, v, w) can still relax:
#     ➜ Negative weight cycle exists

# Time: O(N * E), Space: O(N)

# Logic for negative cycle -> when after the n-1 iterations, weights in distance array will still decrease because of negative
# cycle

# This function is returning bool for negative cycles and distances array(Shortest path from source for every node)
def bellmann_ford(source, edge_list, n):
  distance = [float('inf')] * n
  distance[source] = 0
  for _ in range(n):
    for s, d, weight in edge_list:
      if distance[s] == float('inf'):
        continue
      if distance[s] + weight < distance[d]:
        distance[d] = distance[s] + weight
  
  # For negative cycle detection
  for s, d, weight in edge_list:
    if distance[s] == float('inf'):
      continue
    if distance[s] + weight < distance[d]:
      distance[d] = distance[s] + weight
      return True, distance
  return False, distance

# Takes in source, edge list, number of nodes
print(bellmann_ford(0, [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], 6)) # (False, [0, 5, 3, 3, 1, 2])




