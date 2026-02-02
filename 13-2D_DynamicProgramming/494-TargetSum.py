# *** - Study Tabulation for this problem(TRICKY)
# Recursion
# This question kind of follows same logic as com sum 1(backtracking) but here the total sum can be negative before 
# reaching the total(-1+1+1+1+1=3, after first recursion call amount is -ve). so, no if codn like if amount - nums[index] >= 0 is required

# Base case - when it reaches len(nums) [LAST] and amount is 0 return 1 if amount is not 0 and index is LAST then return 0
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def targetSum(index, amount):
            # if index == len(nums) and amount != 0:
            #     return 0
            # if index == len(nums) and amount == 0:
            #     return 1

            if index == len(nums):
                return 1 if amount == 0 else 0
            
            # Positive nums[i]
            a = targetSum(index+1, amount-nums[index]) 
            # Negative nums[i]
            b = targetSum(index+1, amount+nums[index])

            return a + b
        
        return targetSum(0,target)

# Memoization DP
# Here you have to think, dp array won't work here. amount in recursion can be negative, this will give index out of bounds error
# So, to prevent that, we use dict (amount, index) -> value eg:- dp[(index, amount)] =  value
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}
        def targetSum(index, amount):
            if index == len(nums):
                return 1 if amount == 0 else 0
            
            if (index, amount) in dp:
                return dp[(index, amount)]
            
            # Positive nums[i]
            a = targetSum(index+1, amount-nums[index]) 
            # Negative nums[i]
            b = targetSum(index+1, amount+nums[index])

            dp[(index, amount)] =  a + b
            return dp[(index, amount)]
        
        return targetSum(0,target)

# Tabulation DP [NOT UNDERSTOOD!!!]
# Here, we face the same issue, amount can be -ve
# but we need a array for tabulation so, use [{} for index in range(len(nums))]
# use defaultDict to access it like a array
# for every index from 0 to n-1 there will be amount(0,amount)
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = [defaultdict(int) for index in range(len(nums)+1)]
        # Base case
        dp[len(nums)][0] = 1
        for i in range(len(nums) - 1, -1, -1):
            for curr_sum, ways in dp[i+1].items():
                dp[i][curr_sum + nums[i]] += ways
                dp[i][curr_sum - nums[i]] += ways
        return dp[0][target]
            
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1,1,1,1,1],3))
    print(s.findTargetSumWays([1],1))
    