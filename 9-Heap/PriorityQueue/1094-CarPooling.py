import heapq

# Min Heap
# TRICKY QUESTION
# Logic: sort the trips by start location
# use a min_heap to keep track of (end_time, num_pass)
# tranverse the trips(array sorted by start location), add numPass to currentPass and if any start location is more than min-heap end location, pop from the min-heap and reduce currentPass by numPass
# if at any point currentPass > capacity, return False
# nlogn and n

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key = lambda trip: trip[1])

        min_heap = []
        for numPass, _, end in trips:
            min_heap.append((end, numPass))
        
        heapq.heapify(min_heap)
        
        currentPass = 0
        
        for numPass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, passengers = heapq.heappop(min_heap)
                currentPass -= passengers
            
            currentPass += numPass

            if currentPass > capacity:
                return False
        
        return True

# Prefix arr Method
# This is not exactly prefix arr but every similar to that
# Form a array till last position(Take max 'to' from the question)
# At every 'from', add numPass at that position and subtract numPass at 'to' position
# At last, add the res arr to find the num of passengars at every position
# currPass > Capacity, return False
# else return True

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # max 'to' is 1000
        res = [0]* 1001

        for numPass, start, end in trips:
            res[start]+= numPass
            res[end] -= numPass
        
        currentPass = 0
        for passengers in res:
            currentPass += passengers
            if currentPass > capacity:
                return False
        
        return True
            

