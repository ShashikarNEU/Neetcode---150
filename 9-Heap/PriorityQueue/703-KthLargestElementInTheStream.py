import heapq
# https://www.youtube.com/watch?v=hOjcdrqMoQ8
# [TRICKY QUESTION] This is a very tricky question to understand -> [REVISE]
# Think of two representations here -> min heap representation and Descending order(nums)
# From the descending order reprentation, for the kth largest, we need only k numbers and it is the last number of the bunch
# How to elimnate all the other min numbers thenn-> min heap
# Array size will be equal to k or greater than k
# whenever the size exceeds k, you just minheap pop() 
# when it is of size k, return the last elment in descending order(i.e, MIN HEAP ROOT)
class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
            

        
        