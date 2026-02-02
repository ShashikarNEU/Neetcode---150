# Recursion 
# Recursion soln is almost as same as coin change 1, the tricky part is that we will recount similar combinations
# using that appoarch eg like [1,2,2], [2,1,2], [2,2,1] - all same. This is possible if we use for loop from i -> n in every recursion call
# To avoid it, pass index as a argument and do index -> n in every recursion call. This way, we can avoid repeatations(only [1,2,2] will be counted here)
# That's why this problem is 2d DP
# Recursion - with for loop
from typing import List


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        def coinChange(amount, index):
            if amount == 0:
                return 1
            totalWays = 0
            for i in range(index, len(coins)):
                if amount - coins[i] >= 0:
                  totalWays += coinChange(amount - coins[i], i)
            return totalWays
        return coinChange(amount, 0)

# Recursion - without for loop [Optimal one]
# This recursion is same as combination sum 1 (Backtracking series)
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        def coinChange(amount, index):
            if amount == 0:
                return 1
            
            a = coinChange(amount-coins[index], index) if amount - coins[index] >= 0 else 0
            b = coinChange(amount, index+1) if index + 1 < len(coins) else 0

            return a+b

        return coinChange(amount, 0)

# Memoization DP
# DP Array has to be mirrored with recursion fn
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins)+1)]
        def coin(i, target):
            if target == 0:
                return 1
            if i == len(coins) or target < 0:
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            
            take = coin(i, target-coins[i])
            skip = coin(i+1, target)

            dp[i][target] =  take+skip
            return dp[i][target]
        return coin(0, amount)

# Tabulation DP
# We go from base case to the answer
# dp[amount=0][index]= 1 to dp[amount][0]
# index i means from that index, to n-1 for current amount, how many ways?

# We are going from last index to first because we need dp[amount][index+1] in some cases[IMP]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for i in range(n+1)]

        for i in range(n,-1,-1):
            for target in range(amount+1):
                if target == 0:
                    dp[i][target] = 1
                    continue
                
                if (i == n and target != 0):
                    dp[i][target] = 0
                    continue
                    
                res = 0
                res += dp[i][target-coins[i]] if target - coins[i] >= 0 else 0
                res += dp[i+1][target]
                dp[i][target] = res
        
        return dp[0][amount]

        
                
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.change(5,[1,2,5]))
    print(s.change(3,[2]))
    print(s.change(10,[10]))
    