# FOLLOW UP TO 703 - Kth Largest Element in the stream

# They want largest element in the array. Think of two representations - descending and min heap
# We only want k numbers in the descending order and last of that numbers in the answer so, numbers after 
# that are waste - remove them. Use min heap pop() to remove when length>k. now, last of the num in decending order
# is the min of the whole heap so, return heap[0] as the answer

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]