# SLIGHTLY TRICKY QUESTION (THINK OF HOW TO USE 2D DP HERE)
# [1,2,3,0,2]
# Wrong solution/Appoarch
# Here, this appoarch is good but not fully correct
# this is following a greedy appoarch, take every i and finding max from there and enforcing cooldown. REpeat this till
# we reach the end
# But we should have a choice of whether to skip and take that particular i(Buy). Explore all possiblities.
# Incorrect Soln (185/210 test cases passed)
from typing import List


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        def profit(i):
            if i >= n-1:
                return 0
            max_profit = 0
            for j in range(i+1,n):
                max_profit = max(max_profit, (prices[j] - prices[i]) + profit(j+2))
            return max_profit
        return max(profit(i) for i in range(len(prices)))

# Recursion
# But we should have a choice of whether to skip and take that particular i(Buy). Explore all possiblities.
# so, have a holding variable and do hold=1 or hold=0. then buy, don't buy(hold = 0) and sell, don't sell(hold = 1)
# rest of the logic is same as com sum
# if sold, enforce cooldown
# we can't buy or don't sell at n-1 index but max() return will take care of it. max of the values will be returned
# so no if codn needed. it will compute rec(i+2) and rec(i+1) at buy. don't sell at i+1 index but it will decrease the value and it won't returned
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        def profit(i, holding):
            if i >= n:
                return 0
            if holding == 0:
                buy = -prices[i] + profit(i+1,1) 
                dont_buy = profit(i+1,0)
                return max(buy, dont_buy)
            else:
                sell = prices[i] + profit(i+2,0)
                dont_sell = profit(i+1,1) 
                return max(sell, dont_sell)
            
        return profit(0,0)

# Memoization DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+2)]
        def profit(i, holding):
            if i >= n:
                return 0
            if dp[i][holding] != -1:
                return dp[i][holding]
            if holding == 0:
                buy = -prices[i] + profit(i+1,1) 
                dont_buy = profit(i+1,0)
                dp[i][holding] = max(buy, dont_buy)
                return dp[i][holding]
            else:
                sell = prices[i] + profit(i+2,0)
                dont_sell = profit(i+1,1) 
                dp[i][holding] = max(sell, dont_sell)
                return dp[i][holding]
            
        return profit(0,0)

# Tabulation DP
# instead of adding if codn checks for all, expand dp index size by 2 till n+2. Everything will be contained.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for i in range(n+2)]
        for i in range(n+1,-1,-1):
            for holding in range(1,-1,-1):
                if i >= n and holding == 0:
                    dp[i][holding] = 0
                    continue
                
                if i >= n and holding == 1:
                    dp[i][holding] = float('-inf')
                    continue
                
                if holding == 0:
                    buy = -prices[i] + dp[i+1][1]
                    dont_buy = 0 + dp[i+1][holding]
                    dp[i][holding] = max(buy,dont_buy)
                elif holding == 1:
                    sell = prices[i] + dp[i+2][0]
                    dont_sell = 0 + dp[i+1][holding]
                    dp[i][holding] = max(sell,dont_sell)
        
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]))
    print(s.maxProfit([1]))
        