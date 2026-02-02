# Good Question
# We can solve this with for loop or com sum way
# for loop way - from index, do for loop and check for LIS with if codn(if nums[j] > nums[i] max(1,1+LIS(j))). if codn will act as a return statement. return if index == last is not needed here as seq can end before that also and besides if condn will stop it. have maxLIS = 1, if the maxLIS is not there then, it won't go inside if condn and maxLIS will have the default value(float('-inf')) or else you can calculate max outside if codn
# for calling the method, LIS can start from 0 to n-1. take max of that. LIS can start from any index 

# Recursion
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def LIS(index):
            maxLIS = 1
            for j in range(index, len(nums)):
                if nums[j] > nums[index]:
                    maxLIS = max(maxLIS, 1 + LIS(j))
            return maxLIS
        return max(LIS(i) for i in range(len(nums)))
    
# Memoization
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        def LIS(index):
            maxLIS = 1
            if dp[index] != -1:
                return dp[index]
            for j in range(index, len(nums)):
                if nums[j] > nums[index]:
                    maxLIS = max(maxLIS, 1 + LIS(j))
            dp[index] = maxLIS
            return dp[index]
        return max(LIS(i) for i in range(len(nums)))

# Tabulation DP
# Think of the logic
# but copy everything from memiozation
# for max(LIS(i) for i in range(len(nums))) it's max(dp) in tab [THINK]
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            maxLIS = 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    maxLIS = max(maxLIS, 1+dp[j])
            dp[i] = maxLIS

        return max(dp)

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([1,2,4,3]))
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([0,1,0,3,2,3]))
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))


            