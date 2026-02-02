# Same min heap pattern as lc 1094 - car pooling
# Can't use diff arr + prefix sum pattern due to input length up to 10^5

# Sort the input
# in these kinds of range questions where we need to find a capacity at a point in time, 
# we can usually min heap or prefix sum
# Add the start times one by one and form a min heap of the end times
# if start > end, pop it decrement the count by 1
# do it in while loop(popping and decrementing(what if there are many))

import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda interval: interval[0])
        min_heap = []
        for _, end in intervals:
            min_heap.append(end)
        
        heapq.heapify(min_heap)
        current_rooms = 0
        maxRooms = float('-inf')

        for start, end in intervals:
            while min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
                current_rooms-=1

            current_rooms += 1
            maxRooms = max(maxRooms, current_rooms)
        
        return maxRooms