from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0
        maxProfit = 0
        
        while p2 < len(prices):
            if prices[p2]-prices[p1] > 0:
                profit = prices[p2]-prices[p1]
                maxProfit = max(maxProfit, profit)
            else:
                p1 = p2

            p2+=1
        
        return maxProfit

if __name__ == "__main__":
  s = Solution()
  print(s.maxProfit([7,1,5,3,6,4])) 
         