# First Way to Solve this > Varition of Djikstra
# https://www.youtube.com/watch?v=vWgoPTvQ3Rw
# Varition of djikstra algo - I added path length to djikstra min heap also
# We don't need a visiting set here as we need allow same node multiple times into the heap. if there is a path with greater weight but less path length, we should consider that path also. so, visited[node] array to track distance and if visited[node] < pathLength but more weight -> push it into the heap

# 2 cases to consider here
# Only revist nodes, if one of following applies
# 1. min weight for that node(First time for that node)
# 2. if more weight but less stops than the previous path( Will leads to easier path)

# [HINT] sometimes, choosing more weight will leds you down a easier path to the dst(of min cost)
# See, from min path to k given, we will get other paths with higher cost, but what if these path go down a easier path(min cost)

import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]

        for source, destination, price in flights:
            adj_list[source].append((destination, price))
        
        min_heap = []
        min_heap.append((0, 0, src)) # distance from source, path length from source, starting node
        visited = [float('inf')] * n
        
        while min_heap:
            price_prev, path_length, node = heapq.heappop(min_heap)
           
            # 2 cases considered here
            if path_length - 1 > k or path_length > visited[node]:
                 continue

            if node == dst:
                return price_prev
            
            visited[node] = path_length

            neighbours = adj_list[node]
            for neighbour, price in neighbours:
                    heapq.heappush(min_heap, (price_prev + price, path_length + 1, neighbour))
        
        return -1 # Disconnected graph
    
# Second Way to solve this - Bellman Ford Algo
# Refer Bellmann ford first
# https://neetcode.io/solutions/cheapest-flights-within-k-stops
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
    print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
    print(s.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))
