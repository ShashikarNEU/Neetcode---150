# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        hash_map = {}

        def dfs(node):
          node_copy = Node(node.val)
          hash_map[node] = node_copy
          for node_neighbors in node.neighbors:   
              if node_neighbors not in visited:
                 visited.add(node_neighbors)
                 node_copy = dfs(node_neighbors)
                 node_copy.neighbors.append(hash_map[node_neighbors])
          return node_copy
        
        return dfs(node)
    
class Solution:    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = {}  # Maps original nodes to their cloned versions
        
        def dfs(node):
            if node in hash_map:
                return hash_map[node]  # Return already created clone
            
            # Create a clone of the node
            node_copy = Node(node.val)
            hash_map[node] = node_copy  # Store in map
            
            # Clone all neighbors
            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))  # Append cloned neighbors
            
            return node_copy
        
        return dfs(node)

        

        