# Kadane algo
# keep track of the sum, max sum
# if sum is -ve then, reset it to 0 and then start again
# EDGE CASE:- record max sum before resetting negative sum to zero
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane algo
        max_sum = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
            
        return max_sum