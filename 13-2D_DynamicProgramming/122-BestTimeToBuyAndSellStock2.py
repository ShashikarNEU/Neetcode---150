# Recursive
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        def maxP(index, holding):
            if index >= n:
                return 0
            if holding == 0:
                buy = -prices[index] + maxP(index+1,1)
                dont_buy = 0 + maxP(index+1,0)
                return max(buy, dont_buy)
            else:
                sell = prices[index] + maxP(index+1,0)
                dont_sell = 0 + maxP(index+1,1)
                return max(sell,dont_sell)
        
        return maxP(0,0)


# Memoization DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+2)]
        def maxP(index, holding):
            if index >= n:
                return 0
            if dp[index][holding] != -1:
                return dp[index][holding]
            if holding == 0:
                buy = -prices[index] + maxP(index+1,1)
                dont_buy = 0 + maxP(index+1,0)
                dp[index][holding] = max(buy, dont_buy)
            else:
                sell = prices[index] + maxP(index+1,0)
                dont_sell = 0 + maxP(index+1,1)
                dp[index][holding] = max(sell,dont_sell)
            return dp[index][holding]
        
        return maxP(0,0)

#  Tabulation DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]  # n+1 because we check index+1
        
        for index in range(n, -1, -1):
            for holding in range(2):
                if index >= n:
                    dp[index][holding] = 0
                    continue
                if holding == 0:
                    buy = -prices[index] + dp[index+1][1]
                    dont_buy = 0 + dp[index+1][0]
                    dp[index][holding] = max(buy, dont_buy)
                else:
                    sell = prices[index] + dp[index+1][0]
                    dont_sell = 0 + dp[index+1][1]
                    dp[index][holding] = max(sell, dont_sell)
        
        return dp[0][0]

# Greedy Appoarch
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        
        return profit
