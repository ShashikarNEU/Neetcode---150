# We solve this using DP also(TRY IT LATER!!)

# But using greedy is better and more efficient
# Logic: check i+nums[i] first, it's max_reach then do i+nums[i] == i then, max_reach is that index itself -> return False
# i+nums[i] >= len(nums)-1 then return True

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = float('-inf')
        for i,num in enumerate(nums):
            max_reach = max(max_reach, i+num)
           
            if max_reach >= len(nums)-1:
                return True
            if max_reach == i:
                return False
        
        return False

        