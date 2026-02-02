# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

# https://takeuforward.org/plus/dsa/problems/frog-jump

# This logic is similar to min cost stairs leetcode but it has one extra base case
# In n-2 recursion call, it will give index out of bounds error for 2 steps so, handle that
# Refer that first [746-minCostStairs]

# You can add if index ==  n-2 base case or if index+2 < n avoid index out of bounds error [Your wish]
# I commented out the n-2 base case

# Recursion
class Solution_Rec:
    def frogJump(self, heights):
        
        def frogJump(index):
            # Base cases
            if index == len(heights)-1:
                return 0
            # if index == len(heights)-2:
            #     return abs(heights[len(heights)-1] - heights[len(heights)-2])
            
            one_step_cost = abs(heights[index+1] - heights[index]) + frogJump(index+1)
           
            two_step_cost = abs(heights[index+2] - heights[index]) + frogJump(index+2) if index + 2 < len(heights) else float('inf')
            
            return min(one_step_cost, two_step_cost)
        
        return frogJump(0)

# Tabulation DP(Easy because of recursion)
# Made careless mistake on my first attempt here, I took i-1 as going up wrongly but it was i+1 since we start from the last
class Solution_tab:
    def frogJump(self, heights):
        n = len(heights)
        dp = list(heights)
        dp[n-1] = 0
        dp[n-2] = abs(heights[n-1] - heights[n-2])

        for i in range(n-3,-1,-1):
            dp[i] = min(abs(heights[i+1] - heights[i]) + dp[i+1], abs(heights[i+2] - heights[i]) + dp[i+2])
        print(dp)
        
        return dp[0]
    
# Simple follow up -> it can make k jumps, instead of 1 or 2
# In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.
class Solution_Kjumps:
    def frogKJumps(self, heights, k):
        n = len(heights)
        def frogKJump(index):
            if index == n-1:
                return 0
        
            min_cost = float('inf')
            for i in range(1,k+1):
                # This can go out of range so, this line (We can add this)
                if index + i < n:
                  i_jump = abs(heights[index] - heights[index+i]) + frogKJump(index+i)
                  min_cost = min(min_cost, i_jump)
            return min_cost
        
        return frogKJump(0)

# Tabulation DP
class Solution_Kjumps_tab:
    def frogKJumps(self, heights, k):
        dp = list(heights)
        n = len(heights)
        dp[n-1] = 0
        dp[n-2] = abs(heights[n-1]-heights[n-2]) + 0

        for i in range(n-3,-1,-1):
            min_cost = float('inf')
            for j in range(1,k+1):
                if i+j < n:
                    i_jump = abs(heights[i]-heights[i+j]) + dp[i+j]
                    min_cost = min(i_jump, min_cost)
            dp[i] = min_cost
        
        return dp[0]
               
# Test cases
if __name__ == "__main__":
    solution_Rec = Solution_Rec()
    solution_tab = Solution_tab()
    solution_Kjumps = Solution_Kjumps()
    solution_Kjumps_tab = Solution_Kjumps_tab()
    print("Frog Jump")
    print("--------------------------")
    print("Recursion")
    print(solution_Rec.frogJump([2, 1, 3, 5, 4]))
    print(solution_Rec.frogJump([7, 5, 1, 2, 6]))
    print("Tabulation DP")
    print(solution_tab.frogJump([2, 1, 3, 5, 4]))
    print(solution_tab.frogJump([7, 5, 1, 2, 6]))

    print("\nFrog K Jumps")
    print("--------------------------")
    print("Recursion")
    print(solution_Kjumps.frogKJumps([10, 5, 20, 0, 15],2))
    print(solution_Kjumps.frogKJumps([15, 4, 1, 14, 15],3))
    print("Tabulation DP")
    print(solution_Kjumps_tab.frogKJumps([10, 5, 20, 0, 15],2))
    print(solution_Kjumps_tab.frogKJumps([15, 4, 1, 14, 15],3))   