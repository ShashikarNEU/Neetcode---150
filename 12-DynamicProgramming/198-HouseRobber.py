# https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6 (WATCH First 8 mins for hint!!)
# Recursion
# For this logic, think about subsequences/subsets problems in backracking series [HINT!!]
# for on element, we can take it and next i+2 elment till the end
# or we don't take it and move on to the next element
# This way, we can start from every element go in a alternating path till the end
# Finally, take max of the two paths
class Solution:
    def rob(self, nums: list[int]) -> int:
        def houseRob(index):
            if index >= len(nums):
                return 0
            # Take this index
            a = nums[index] + houseRob(index + 2)
            # Don't take this index
            b = 0 + houseRob(index + 1)
            return max(a,b)
            
        return houseRob(0)

# Memoization
class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [-1]*len(nums)
        def houseRob(index):
            if index >= len(nums):
                return 0
            
            if dp[index] != -1:
                return dp[index]
          
            # Take this index
            a = nums[index] + houseRob(index + 2)
            # Don't take this index
            b = 0 + houseRob(index + 1)
            dp[index] =  max(a,b)
            return dp[index]
            
        return houseRob(0)

# Think about the pattern using recursion first
# Tabulation DP
# Last 2 houses are base cases(Meaning if only last were present, then values of indexes are the answer!!)
# TRICK one, dp[n-2] is also max(dp[n-1],dp[n-2]) [THINK!!]
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dp = list(nums)
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2],nums[n-1])
        for i in range(n-3,-1,-1):
            dp[i] = max(dp[i] + dp[i+2], dp[i+1])
        return dp[0]

# Tabulation
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        dp[n] = 0
        dp[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,1,1,2]))
    print(s.rob([2,7,9,3,1]))
