# Problem statement
# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

# For Example :
# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.

# Sample Input 1:
# 2
# 4 5
# 4 3 2 1
# 5 4
# 2 5 1 6 7
# Sample Output 1:
# true
# false
# Explanation For Sample Input 1:
# In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
# In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
# Sample Input 2:
# 2
# 4 4
# 6 1 2 1
# 5 6
# 1 7 2 9 10
# Sample Output 2:
# true
# false
# Explanation For Sample Input 2:
# In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
# In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.

# Recursion
# Use subset backtracking technique
# but instead of empty, use target and make it 0 via recursion
# You can start from 0 or n-1(Your mood)
# For False base case, since index == -1 is not possible is dp arr, we write when index == 0, target has to be equal to nums[index](nums[0]) for it to be True if not, return False. So, To summarize this, write if index == 0: return nums[index] == target
def subsetSum(arr, k):
  def subsetS(index, target):
    if target == 0:
      return True
    if index == 0:
      return target == arr[index]
    # if index < 0 and target != 0:
    #   return False
    take = subsetS(index - 1, target - arr[index]) if target - arr[index] >= 0 else False
    notTake = subsetS(index - 1, target)
    return take or notTake
  return subsetS(len(arr)-1,k)

# Memoization DP
def subsetSum(arr, k):
  dp = [[None]*(k+1) for _ in range(len(arr))]
  def subsetS(index, target):
    if dp[index][target] != None:
      return dp[index][target]
    if target == 0:
      return True
    if index < 0 and target != 0:
      return False
    take = subsetS(index - 1, target - arr[index]) if target - arr[index] >= 0 else False
    notTake = subsetS(index - 1, target)
    dp[index][target] =  take or notTake
    return dp[index][target]
  return subsetS(len(arr)-1,k)

# Tabulation DP
# We start from the base cases and go the subsetSum(n-1,k)
# For False base case, since index == -1 is not possible is dp arr, we write when index == 0, target has to be equal to nums[index](nums[0]) for it to be True if not, return False. So, To summarize this, write if index == 0: return nums[index] == target
def subsetSum(arr, k):
  dp = [[None]*(k+1) for _ in range(len(arr))]
  for index in range(len(arr)):
    for target in range(k+1):
      # For True base case
      if target == 0:
        dp[index][target] = True
        continue
      # For False base case
      if index == 0:
        dp[index][target] = (target == arr[index])
        continue
      
      take = dp[index-1][target-arr[index]] if target - arr[index] >= 0 else False
      notTake = dp[index-1][target]
      dp[index][target] = take or notTake
  return dp[len(arr)-1][k]
      
# Test cases
if __name__ == "__main__":
    print(subsetSum([6,1,2,1],4))
    print(subsetSum([1,7,2,9,10],6))
    