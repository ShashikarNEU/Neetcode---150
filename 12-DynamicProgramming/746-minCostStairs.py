# https://neetcode.io/solutions/min-cost-climbing-stairs
# Since, question starts from the start, we also start from the start
# For this question, apply previous principles and draw decision tree first
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def minCostStairs(i):
            if i >= len(cost):
                return 0
            
            one_step_cost = minCostStairs(i+1) + cost[i]
            two_step_cost = minCostStairs(i+2) + cost[i]

            return min(one_step_cost, two_step_cost)
        
        return min(minCostStairs(0), minCostStairs(1))

# Memoization DP (Top Down DP)
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [-1] * len(cost)
        def minCostStairs(n):
            if n > len(cost) - 1:
                return 0
            if dp[n] != -1:
                return dp[n]
            left = minCostStairs(n+1) + cost[n]
            right = minCostStairs(n+2) + cost[n]
            dp[n] = min(left, right)
            return dp[n]
        
        # We are outside first, so he can hop on 0th index or 1th index[TRICKY]
        return min(minCostStairs(0), minCostStairs(1))

# Tabulation DP
# For finding the pattern behind tabulation, find base case and try to build the other n from baser case, look for a pattern there
# Now repeat it for all n

# Here we are solving it from reverse
# [10, 15, 20] 0(Goal)
# 20, 0 are the base cases and build it from reverse

# for n-2 case, the way to reach the goal is dp[n-2] = min(dp[n-2] + one step dp[n-1], dp[n-2] + two step dp[n])
# Now repeat this for all other n
# base case
# dp[n] = 0 # already at the goal
# dp[n-1] = cost[n-1] # one step to goal

# Tabulation
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n+2)
        dp[n] = 0 # already at the goal
        dp[n-1] = cost[n-1] # one step to goal
        for i in range(n-2,-1,-1):
            dp[i] = min(dp[i+1]+cost[i], dp[i+2]+cost[i])

        return min(dp[0],dp[1])
        
# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]))
            