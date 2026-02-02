from collections import defaultdict
import heapq

# Form a hasMap of unique values from x array to have y values
# make a heap out of every list
# take max of those lists(heap[0] in maxheap) and form a result list
# take the sum of first elements from that result list
class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        hashMap = defaultdict(list)

        for i in range(len(x)):
            heapq.heappush(hashMap[x[i]], -1*y[i])
        
        heap_list = hashMap.values()
        if len(heap_list) < 3:
            return -1
        result_list = [-1*heap[0] for heap in heap_list]
         
        return sum(sorted(result_list, reverse=True)[:3])
            
        
