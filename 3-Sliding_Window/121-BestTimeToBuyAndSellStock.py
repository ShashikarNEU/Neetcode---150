class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p1 = 0
        p2 = 0
        profit = 0
        max_profit = 0
        while p2 < len(prices):
            while prices[p2]-prices[p1] < 0:
                p1+=1
            profit = prices[p2]-prices[p1]
            max_profit = max(profit, max_profit)
            p2+=1
        return max_profit

if __name__ == "__main__":
  s = Solution()
  print(s.maxProfit([7,1,5,3,6,4])) 
         