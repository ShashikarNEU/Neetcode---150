# Refer DP shortcut in intro_dp
# All possible ways, use recursion then, DP
# convert this problem to indexes, i
# for that index, find all possible ways, if reach the end, return 1(success) and if we reach 1, return 1(success and 1 way to reach 0)
# For any given n, we can go by n-2 fn call and n-1 fn call, it will both give some ans, we need to sum it for all possible ways for that index
# This problem is similar to fib seq. for DP optimization, refer that
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 1:
#             return 1
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# For finding tabulation ans, start from n=0 and n=1 case(base case) and go up to other n, n=3, you will find that climbStairs(3) = climbStairs(2) + climbStairs(1). This pattern follows the problem. So, use that to build a Bottom-Top DP Soln.
# Tabulation DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # from 2 to n
        for i in range(2, n+1):
          dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
# Other way (same ans but I am starting from 0 in recursion and memoization then, taking n as base case and going to 0 in tab)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def climb(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            if dp[stair] != -1:
                return dp[stair]
            one_step = climb(stair+1)
            two_step = climb(stair+2)
            dp[stair] =  one_step + two_step
            return dp[stair]

        return climb(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            one_step = dp[i+1]
            two_step = 0 if i+2 > n else dp[i+2]
            dp[i] = one_step + two_step
        return dp[0]

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(1))

        