# https://neetcode.io/solutions/burst-balloons
# for every i in the loop you take it last, left i right. left and right are in the boundaries
# for loop: nums[i]*nums[l-1]*nums[r+1] + rec(l,i-1) + rec(i+1,r)
# Termination -> l > r return 0
# Recursion
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        def maxC(left,right):
            if left > right:
                return 0
            maxCoins = 0
            for i in range(left,right+1):
                coins = nums[i] * nums[left-1] * nums[right+1] 
                coins += maxC(left, i-1) + maxC(i+1,right)
                maxCoins = max(coins, maxCoins)

            return maxCoins
        return maxC(1,len(nums)-2)

# Memoization DP
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def maxC(left,right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            maxCoins = 0
            for i in range(left,right+1):
                coins = nums[i] * nums[left-1] * nums[right+1] 
                coins += maxC(left, i-1) + maxC(i+1,right)
                maxCoins = max(coins, maxCoins)

            dp[(left, right)] = maxCoins
            return dp[(left, right)]
        return maxC(1,len(nums)-2)

# Tabulation DP
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]

if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3,1,5,8]))
    print(s.maxCoins([1,5]))