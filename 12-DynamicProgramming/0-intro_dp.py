# Pls complete backtracking series first (7-backtracking)
# Video reference -> https://www.youtube.com/watch?v=tyB0ztf0DNY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3

# DP has 2 methods - Memoization (Top-Down) and Tabulation (Bottom-Top)
# We can also improve Tabulation SC, leading to a final optimal ans

# Memoization
# Fib Seq
# General recursion fn
# 0 1 1 2 3 5
def fib(n):
  if n <= 1:
    return n
  return fib(n-1)+fib(n-2)

# Recursion Tree for fib(5)
# 
#          fib(5)
#         /      \
#     fib(4)    fib(3)
#     /    \     /    \
# fib(3)  fib(2) fib(2) fib(1)
# /    \        
#fib(2) fib(1)   
# /    \
#fib(1) fib(0)

print("Without DP: ", fib(10))

# As you can you can see, we are repeating the fib() fn call in many areas. since we have the result
# We can store it in a array and retreive it for optimal soln

# Memoization (Top-Down DP) is an optimization technique that stores the results of repeated recursive calls in a cache (usually a dictionary or an array) to avoid redundant computations. It improves the time complexity of recursive solutions by preventing repeated calculations, transforming an exponential-time algorithm into a more efficient polynomial-time one.

# Here, you go from n to base cases, solve them and come on up (Tabulation is opposite)

def fib_dp(n, dp):
  if n <= 1:
    return n
  if dp[n] != -1:
    return dp[n]
  dp[n] = fib_dp(n-1, dp) + fib_dp(n-2, dp)
  return dp[n]

n = 10
# n = 5, we need dp[0] to dp[5] so, 5+1 (n+1)
dp = [-1] * (n+1)
print("DP Memoization: ",fib_dp(10, dp))

# We are having dp array of -1, if dp[n] not -1, return it else, store the recursion call (fib(n-1) + fib(n-2)) in dp[n]
# You can also use dp as global variable instead of passing it as argument

# Time complexity -> O(n) because it's calling f(n) for f(0) to f(n) calls[n times], All repeated calls are O(1)
# Space complexity -> O(n) [Recursion call stack] + O(n)[DP Array] -> O(n)

# Tabulation
# Fib Seq
# Tabulation -> Going from base case(here n=1 and n=0) to the required answer

# Tabulation (Bottom-Up DP) is an approach where we solve a problem iteratively by filling up a table (usually an array) from smaller subproblems to larger ones. It eliminates recursion overhead and ensures each subproblem is solved only once, leading to efficient time and space usage.

# First assign dp[0] = 1 and dp[1] = 1
# Build the array from bottom to top, n

def fib_tabulation_dp(n):
  dp = [0] * (n+1)
  dp[0] = 0
  dp[1] = 1
  # from 2 to n
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

print("DP Tabulation: ",fib_tabulation_dp(10))

# This is for 1-d contraint - only n. some problems have x, y(2-d) as arguments so, for each x,y we have to compute
# it becomes a table if we do that hence it called tabulation

# You can improve the space complexility
def fib_dp_optimal(n):
  n_1_element = 1
  n_2_element = 0

  for i in range(2, n+1):
    result = n_1_element + n_2_element
    n_1_element, n_2_element = n_2_element, n_1_element
    n_1_element = result
  
  return n_1_element

print("DP Tabulation Optimal: ", fib_dp_optimal(10))

# Shortcut to DP problem

# How to understand if it's a DP problem
# if the question asks you to count all possible ways, multiple ways to do this, find min/max of that
# then, we have to use recursion
# if recursion is used -> then, we can use DP -> memoization, tabulation and tabulation optimal 

# How to solve DP problem
# Step 0: Try to decision tree and solve it from there
# Step 1: try to represent the question in terms of index
# Step 2: Do all possible stuff on that index acc to the problem statement
# Step 3: if the question says to 
# 1. find all possible ways -> return sum of all the indexes 
# 2. find min of all possible ways -> return min of the indexes
# 3. find max of all possible ways -> return max of the indexes

# Here index means all possible ways for that index

# Tabulation DP
# For finding the pattern behind tabulation, find base case and try to build the other n from baser case, look for a pattern there
# Now repeat it for all n



