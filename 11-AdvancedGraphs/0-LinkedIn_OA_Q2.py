# LinkedIn OA Question 1 was direct BFS - Easy

# LinkedIn OA Q2 (2025) — Roads Between Cities = (Leetcode 787 + Leetcode 1631)
# --------------------------------------------
# Problem:
# You're given a list of roads between cities. Each road connects two cities and has a cost.
# Given a source city, destination city, and a max road length `k`,
# find the **minimum possible max-edge-cost** among all valid paths from source to destination
# such that the **number of edges in the path ≤ k**.
#
# Definition:
# - The cost of a path is defined as the **maximum edge cost** in that path.
# - Among all valid paths (with ≤ k edges), return the **minimum such path cost**.
#
# Input:
# - edge_list: List of [u, v, cost] representing bidirectional roads
# - source: int
# - destination: int
# - k: int (max path length in terms of number of edges)
#
# Output:
# - An integer: min(max_edge_cost) across all valid paths from source to destination with ≤ k edges
# - If no such path exists, return -1
#
# Constraints:
# - No self-loops or duplicate edges
# - Positive edge weights

import heapq
def minCost(n, roads, source, dest, k):
  adj_list = [[] for _ in range(n)]

  for u, v, cost in roads:
    adj_list[u].append((v, cost))
    adj_list[v].append((u, cost))
  
  min_heap = []
  min_heap.append((0, 0, 0)) # Cost, Path Length, Starting Node
  distance = [float('inf')] * n

  while min_heap:
    road_cost_prev, path_length, node = heapq.heappop(min_heap)

    if path_length > k or path_length > distance[node]:
      continue

    distance[node] = path_length

    if node == dest:
      return road_cost_prev

    roads = adj_list[node]

    for neighbour_road, cost in roads:
      road_cost = max(road_cost_prev, cost)
      heapq.heappush(min_heap, (road_cost, path_length + 1, neighbour_road))
  
  return -1


def main():
    # Test Case 1: Basic Case (Simple graph, valid path)
    n = 4
    roads = [
        (0, 1, 4),
        (1, 2, 5),
        (2, 3, 6),
        (0, 3, 8)
    ]
    source = 0
    dest = 3
    k = 3
    print(minCost(n, roads, source, dest, k))  # Expected result: 6
    
    # Test Case 2: Path Length Constraint (No valid path due to k constraint)
    n = 4
    roads = [
        (0, 1, 4),
        (1, 2, 5),
        (2, 3, 6),
        (0, 3, 8)
    ]
    source = 0
    dest = 3
    k = 2
    print(minCost(n, roads, source, dest, k))  # Expected result: 8
    
    # Test Case 3: No Path Exists (Disconnected Graph)
    n = 4
    roads = [
        (0, 1, 4),
        (1, 2, 5)
    ]
    source = 0
    dest = 3
    k = 3
    print(minCost(n, roads, source, dest, k))  # Expected result: -1
    
    # Test Case 4: Multiple Paths (Path with minimum max edge cost)
    n = 5
    roads = [
        (0, 1, 4),
        (1, 2, 5),
        (2, 3, 6),
        (3, 4, 7),
        (0, 3, 9),
        (1, 4, 10)
    ]
    source = 0
    dest = 4
    k = 3
    print(minCost(n, roads, source, dest, k))  # Expected result: 9
    
    # Test Case 5: Path with Max Cost Exactly Equal to k Length
    n = 3
    roads = [
        (0, 1, 1),
        (1, 2, 2),
        (0, 2, 3)
    ]
    source = 0
    dest = 2
    k = 2
    print(minCost(n, roads, source, dest, k))  # Expected result: 2
    
    # Test Case 6: Edge Case (Single Node, No Path)
    n = 1
    roads = []
    source = 0
    dest = 0
    k = 0
    print(minCost(n, roads, source, dest, k))  # Expected result: 0
    
    # Test Case 7: Graph with Multiple Edges Between Nodes (Duplicates)
    n = 4
    roads = [
        (0, 1, 2),
        (0, 1, 3),
        (1, 2, 4),
        (2, 3, 5)
    ]
    source = 0
    dest = 3
    k = 3
    print(minCost(n, roads, source, dest, k))  # Expected result: 5
    
    # Test Case 8: Large Graph with No Valid Path
    n = 100
    roads = [
        (i, i+1, 1) for i in range(99)
    ]
    source = 0
    dest = 99
    k = 50
    print(minCost(n, roads, source, dest, k))  # Expected result: -1
    
    # Test Case 9: Large Graph with Valid Path
    n = 5
    roads = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (0, 2, 2),
        (1, 3, 2)
    ]
    source = 0
    dest = 4
    k = 4
    print(minCost(n, roads, source, dest, k))  # Expected result: 1
    
    # Test Case 10: Graph with Maximum Possible Edge Cost in Path
    n = 5
    roads = [
        (0, 1, 100),
        (1, 2, 50),
        (2, 3, 25),
        (3, 4, 10),
        (0, 4, 200)
    ]
    source = 0
    dest = 4
    k = 3
    print(minCost(n, roads, source, dest, k))  # Expected result: 200

if __name__ == "__main__":
    main()







  