# Sliding window pattern
# Two types - fixed window and dynamic window
# Fixed window -> we use this when the questions gives us the fixed k and we need to find the soln from 
# consective indexes in a array or a string. Have a fixed window of size k and move it forward by adding 
# the next int from the window and subtracting the previous int from the window. keep a min or max to store the
# windows soln
# Example: max sum subarray of size k
def max_sum_subarr(arr,k):
  window_sum = sum(arr[:k]) # Using sum for finding arr sum up to index k
  max_sum = 0
  for i in range(len(arr)-k):
    window_sum-=arr[i] # subtracting the first index from the window
    window_sum+=arr[i+k] # adding the next index from the window
    max_sum = max(window_sum,max_sum)
  return max_sum

# Fixed sliding window pattern --> [imp]
# for i in range(len(s2)-window+1):
#     for j in range(i,i+window):

# Variable-Size (Dynamic) Sliding Window
# When the window size is not fixed and depends on meeting a specific condition 
# (e.g., achieving a certain sum, containing unique characters, etc.).
# Have p1 at 0 and p2 at 1. keep on incrementing p2 as long as the profit is positive. if profit is negative, that means that  new lowest has found
# so, make p1 = p2 and increment p2. repeat this process while recording maxProfit.

# Example Problem: Best Time to buy and sell stock - https://www.youtube.com/watch?v=GaXwHThEgGk&t=56s
def maxProfit(self, prices: list[int]) -> int:
    p1 = 0
    p2 = 1
    profit = 0
    max_profit = 0
    while p2 < len(prices):
        if prices[p2]-prices[p1] > 0:
            profit = prices[p2]-prices[p1]
            max_profit = max(profit, max_profit)
        else:
            p1 = p2
        p2+=1
    return max_profit