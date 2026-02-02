# Tricky Question(using greedy)

# Have left, right pointers
# both start at 0 then, run a loop from left to right and catch max_reach
# update left pointer = old_right + 1
# and new_right = max_reach
# while douing this incrementing res
# if right reaches len(nums)-1 or more -> exit the loop

# Note - Can be solved using 2d DP also

# Tricky question
# Watch video -> https://neetcode.io/solutions/jump-game-ii
class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0
        max_reach = 0

        while r < len(nums)-1:

            for i in range(l,r+1):
                max_reach = max(max_reach, nums[i]+i)
            
            l = r+1
            r = max_reach
            res+=1
        
        return res

