# Djikstra's Algo - Return max(distanceDict.values())
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]
        for u, v, weight in times:
            adj_list[u].append((v, weight))
        
        min_heap = []
        min_heap.append((0, k)) # distance, starting node
        visited = set()
        # This distance dict is from 0 to n-1 so, assign n-1 in algo
        distance_dict = [-1] * (n) # shortest path to every node from source node
        
        while min_heap:
            distance_prev, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            distance_dict[node-1] = distance_prev # Setting shortest path for that node

            neighbours = adj_list[node]
            for neighbour, distance in neighbours:
                heapq.heappush(min_heap, (distance + distance_prev, neighbour))
        
        #print(distance_dict)
        return max(distance_dict) if min(distance_dict) != -1 else -1

        
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
    print(s.networkDelayTime([[1,2,1]], 2, 1))
    print(s.networkDelayTime([[1,2,1]], 2, 2))
