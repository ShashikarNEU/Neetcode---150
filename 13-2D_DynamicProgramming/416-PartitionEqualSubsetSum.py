# FOLLOW UP TO 0-SUBSET SUM EQUALS K 
# Recursion
# Find the total sum. check for total//2 (subsetSum(n-1, total//2))
# if one subset equals k//2, then other subsets also exists with equal sum
# if total sum odd, return False
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def subsetSumPart(index, target):
            if target == 0:
                return True
            if index == 0:
                return target == nums[index]
            
            take = subsetSumPart(index-1,target-nums[index]) if target - nums[index] >= 0 else False
            notTake = subsetSumPart(index-1,target)
            
            return take or notTake
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        return subsetSumPart(len(nums)-1, total//2)

# Memoization DP
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        dp = [[None]*((total//2)+1) for _ in range(len(nums))]
        def subsetSumPart(index, target):
            if target == 0:
                return True
            if index == 0:
                return target == nums[index]
            
            if dp[index][target] != None:
                return dp[index][target]
            
            take = subsetSumPart(index-1,target-nums[index]) if target - nums[index] >= 0 else False
            notTake = subsetSumPart(index-1,target)
            
            dp[index][target] =  take or notTake
            return dp[index][target]
        
        if total % 2 != 0:
            return False
        return subsetSumPart(len(nums)-1, total//2)

# Tabulation DP
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [[None]*((total//2)+1) for _ in range(len(nums))]
        for index in range(len(nums)):
            for target in range((total//2)+1):
                if target == 0:
                    dp[index][target] = True
                    continue
                if index == 0:
                    dp[index][target] = (nums[index] == target)
                    continue
                
                take = dp[index-1][target-nums[index]] if target - nums[index] >= 0 else False
                notTake = dp[index-1][target]
            
                dp[index][target] =  take or notTake
                
        return dp[len(nums)-1][total//2]

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,5,11,5]))
    print(s.canPartition([1,2,3,5]))
    