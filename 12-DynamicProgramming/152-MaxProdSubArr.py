# Brute Force
from typing import List


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxProd = max(nums)
        for i in range(len(nums)):
            res = 1
            for j in range(i, len(nums)):
                res *= nums[j]
                maxProd = max(maxProd, res)
        return maxProd

# Optimal Appoarch
# https://neetcode.io/solutions/maximum-product-subarray
# We should apply kadane algo here
# To find the greatest prod sub arr, we must keep track of the minCurr prod and maxCurrProd along every i of nums
# Because for -ve, -ve * minCurr(which can be -ve) will give the new max. 
# while finding maxCurr and minCurr, if both are +ve for currMin where ith num is -ve and both are -ve for currMax where ith num is +ve then, add i to max() and min() to find curMin and curMax.
# Keep doing this for every i and keep track of the max currMax because it will decrease also
# For 0 case, it will give 0 as currMin, currMax so, put them as 1 to reset it

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        max_prod = max(nums) # if the arr has only -ve products and 0. Ans is 0 so, for that, we take max(nums)
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            
            temp = currMax
            currMax = max(currMax*n, currMin *n, n)
            currMin = min(temp*n, currMin*n, n) # We need the old curr_max not new currMax
            max_prod = max(currMax, max_prod)
        
        return max_prod
               
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))

# Why this problem is solved using Dynamic Programming(Kadane Algo)
# At each index, you must track:
#   - The maximum product ending at that index
#   - The minimum product ending at that index
# Why?
#   -> Because a negative number can turn a minimum product into a maximum product and vice versa.

# The recursion (DP relation) at each index 'i' is:
# max_prod[i] = max(nums[i], nums[i] * max_prod[i-1], nums[i] * min_prod[i-1])
# min_prod[i] = min(nums[i], nums[i] * max_prod[i-1], nums[i] * min_prod[i-1])

# In the optimized version, instead of keeping arrays, we use just two variables.

# So, Kadane's algo is just space optimized tabulation DP.
