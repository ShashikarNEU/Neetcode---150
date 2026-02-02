# O(n2) soln
# Find all subArr, caculate curr sum for every sub arr
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum

# O(n) soln
# Kadane algo - https://www.youtube.com/watch?v=5WZl3MMT0Eg
# it's works like a sliding window(very easy code tho)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
            

                
        