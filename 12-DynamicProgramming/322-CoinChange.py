# Recursion 1
# You can appoarch this via a for loop(DFS), Have amount as a argument and decrease it to 0 but there are cases where amount goes less than zero. so, to prevent that, have a if condn amount - coins[i] >= 0. This way you will eliminate all unnesscary calls(error calls)
# Passes 15/189 cases (becuase of Time limit exceeded error)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def coinC(amount):
            if amount == 0:
                return 0
            minCoins = float('inf')
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    res = 1 + coinC(amount - coins[i])
                    minCoins = min(res, minCoins)
            return minCoins
        
        result = coinC(amount)
        return result if result != float('inf') else -1

# Recursion 2[Better Way]
# You can also appoarch this without the for loop(DFS), do function(index, result) way lly to comSum2 in backtracing section
# To avoid amount going below 0 and index going up len(coins), put if condn for the respective recursion call
# 1 rec call -> repeat same num and subtract amount from that num
# 2 rec call -> go to the next num and ignore current number
# This recursion will create a tree where every possiblity involling these 2 calls exist(lly to comSum1 in backtracking)
# Passes 32/189 cases (becuase of Time limit exceeded error)
# This way is actually the soln for coin change 2 lmao with one small change
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def coinC(index, amount):
            if amount == 0:
                return 0
            
            a = 1 + coinC(index, amount - coins[index]) if amount - coins[index] >= 0 else float('inf')
            b = coinC(index+1, amount) if index+1 < len(coins) else float('inf')
            return min(a,b)
        
        result = coinC(0,amount) 
        return result if result != float('inf') else -1

# Memoization DP
# for non index problem, if we use amount instead of index
# We can use a dict instead of a arr
# You can use 2d array dp also here
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = {}
        def coinC(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            minCoins = float('inf')
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    res = 1 + coinC(amount - coins[i])
                    minCoins = min(res, minCoins)
            dp[amount] =  minCoins
            return dp[amount]
        
        result = coinC(amount)
        return result if result != float('inf') else -1

# in memoization always mirror the dp array with ur recursion call
# if recursion call is rec(i, amount) then dp array is dp[amount][i]
# Better way(2d DP) based on recursion 2 above
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]
        def coin(i, target):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if i == len(coins) and target != 0:
                return float('inf')
            if dp[i][target] != -1:
                return dp[i][target]
            
            a = 1 + coin(i, target - coins[i]) 
            b = coin(i+1, target) 
            dp[i][target] =  min(a,b)
            return dp[i][target]
        result =  coin(0, amount) 
        return -1 if result == float('inf') else result


# Tabulation DP
# Here you can write tabulation for based on recursion 2 memoization also
# https://neetcode.io/solutions/coin-change
# Here we appoarch the problem from front instead of back
# So, dp[0],d[1] to dp[amount] where dp[1] means target is 1, what is the min number of coins from coins to sum to 1?
# for any dp[i], so for any c coin, if you pick c coin then, you need to take dp[i-c] problem since it's already solved(so, 1+dp[i-c])
# take min of all coins for dp[i]. Add a if codn to keep it >= 0 cuz target - c can go below also
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0 # if the target is 0, you don't need to take any coin
        for i in range(1,amount+1):
            minCoins = float('inf')
            for c in coins:
                if i-c >= 0:
                    res = 1 + dp[i-c]
                    minCoins = min(minCoins, res)
            dp[i] = minCoins

        result =  dp[amount]
        #print(dp)
        return result if result != float('inf') else -1

# Other way
# tabulation DP
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]
        for index in range(n, -1, -1):
            for target in range(amount+1):
                if target == 0:
                        dp[index][target] = 0
                        continue
                if index == n:
                    dp[index][target] = float('inf')
                    continue
                
                a = 1 + dp[index][target - coins[index]] if target - coins[index] >= 0 else float('inf')
                
                b = dp[index+1][target]

                dp[index][target] = min(a,b)

        return -1 if dp[0][amount] == float('inf') else dp[0][amount]


# Use 1D DP here
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            
            ans = float('inf')
            for coin in coins:
                res = 1 + dp(rem - coin)
                ans = min(ans, res)
            memo[rem] = ans
            return ans
        
        result = dp(amount)
        return result if result != float('inf') else -1

# Tabulation
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            ans = float('-inf')
            for coin in coins:
                if i-coin >= 0:
                    res = 1 + dp[i-coin]
                    ans = min(ans,res)
        return dp[amount] if dp[amount] != float('-inf') else -1






# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1,2,5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([1], 0))
