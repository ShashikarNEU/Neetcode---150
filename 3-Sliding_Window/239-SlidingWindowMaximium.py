# Brute Force (TC = O((n-k)*k))
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = k
        res = []
        for i in range(len(nums)-window+1):
            max_num = nums[i]
            for j in range(i, i+window):
                max_num = max(max_num, nums[j])
            res.append(max_num) 
        return res

# Using deque data structure [TRICKY]
# in deque, you can pop and popleft(dequeue from both sides)
# deque must be always in montonically decreasing order
# https://neetcode.io/solutions/sliding-window-maximum
# LOGIC
# Have two pointer both at 0 first
# follow dynamic window sliding
# if right pointer num is greater than deque[-1], pop it to maintain a montonically decreasing order
# if smaller, append it. When shifting window, pop from left. Have a codn like left > deque[0] and popleft.  if (r+1)>=k (to ensure that window's size is atleast k), result.append(q[0]) and left+=1
# Understand the pointer logic(How we are shifting the window) and deque logic(always maintain a montonic decreasing deque and leftmost element, add it to result) sperately

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left = 0
        right = 0
        q = deque()
        res = []

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right+1 >= k:
                res.append(nums[q[0]])
                left+=1

            right+=1
        
        return res
            

if __name__ == "__main__":
  s = Solution()
  print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))