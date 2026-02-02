# FOLLOW UP TO HOUSE ROBBER
# Use house rob 1 soln as the base
# For this house rob 2 problem, house are in a circle so, we find the max money earned by leaving first house then by leaving last house after that, take max(1st result, 2nd result) for the answer

# Recursion
from typing import List


class Solution:
    def rob(self, nums: list[int]) -> int:
        def houseRob(arr, index):
            if index >= len(arr):
                return 0
            
            a = arr[index] + houseRob(arr, index+2)
            b = 0 + houseRob(arr, index+1)

            return max(a,b)
        
        # For this house rob 2 problem, house are in a circle so, we find the max money earned by leaving first house then by leaving last house after that, take max(1st result, 2nd result) for the answer
        return max(houseRob(nums[1:], 0), houseRob(nums[:len(nums)-1], 0)) if len(nums) != 1 else nums[0]

# Memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def houseRob(i,arr,dp):
            if i >= len(arr):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(arr[i]+houseRob(i+2,arr,dp),0+houseRob(i+1,arr,dp))
            return dp[i]
        
        return max(houseRob(0,nums[:n-1],[-1]*(n)),houseRob(0,nums[1:],[-1]*n)) if len(nums) != 1 else nums[0] 
        

# Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def houseRob(arr):
            n = len(arr)
            dp = [-1] * (n+1)
            dp[n] = 0
            dp[n-1] = arr[n-1]

            for i in range(n-2,-1,-1):
                dp[i] = max(arr[i]+dp[i+2],0+dp[i+1])
            
            return dp[0]
        
        return max(houseRob(nums[:n-1]),houseRob(nums[1:])) if len(nums) != 1 else nums[0] 

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,1,1,2]))
    print(s.rob([2,7,9,3,1]))
    print(s.rob([2]))
