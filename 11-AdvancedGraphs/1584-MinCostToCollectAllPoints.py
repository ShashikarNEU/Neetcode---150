# Prim's Algo
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        # To store this (x1,y1) and (x2,y2) in adj list, 
        # we are first considering (x1,y1) as one point and (x2,y2) as another point
        # So, assign 0 to n-1 to all the points. then store it in adj list, node 1(x1,y1) 
        # to node 2(x2,y2) with distance (abs(y2-y1)+abs(x2-x1))
        adj_list = [[] for _ in range(n)] # 0 to n-1 nodes
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(y2-y1) + abs(x2-x1)
                adj_list[i].append((j, distance))
                adj_list[j].append((i, distance))

        # Or You can do j loop from 0 to n and have i!=j and add adj[i].append(j, distance) -> Here both directions will be covered
        # for i in range(n):
        #     x1, y1 = points[i]
        #     for j in range(n):
        #         if i != j:
        #           x2, y2 = points[j]
        #           distance = abs(y2-y1) + abs(x2-x1)
        #           adj_list[i].append((j, distance))
        # print(adj_list)

        min_heap = []
        min_heap.append((0, 0)) # distance, starting node
        visited = set()
        min_cost = 0
        while min_heap:
            distance_prev, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            min_cost += distance_prev

            neighbours = adj_list[node]
            for neighbour, distance in neighbours:
                # This line to improve TC(Will work without this line also)
                if neighbour not in visited:
                    heapq.heappush(min_heap, (distance, neighbour))
        
        return min_cost

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
            



                