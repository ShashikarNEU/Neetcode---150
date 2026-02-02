# Introduction To 2D Dynamic Programming / Ninja Training
# https://www.youtube.com/watch?v=AE39gJYuRog&list=PLbgVysG3YYf1vPn2OO1pNrJfHGQXydxX7&index=7

# In this article, we will understand the concept of 2D dynamic programming. We will use the problem ‘Ninja Training’ to understand this concept.

# Problem Statement: A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.

# We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn

# eg:- days = 3 -> This is fixed
# points = [[10,40,70],[20,50,80],[30,60,90]]
# answer = 70(Day 1) + 50(Day 2) + 90(Day 3)

# Recursion
# Using global Variables
def ninjaTraining(points):
  maxPoints = float('-inf')
  
  def ninjaTrain(i,j,totalPoints):
    nonlocal maxPoints
    if i >= len(points):
      maxPoints = max(totalPoints, maxPoints)
      return
    
    for index in range(len(points[i])):
      if index != j:
        # totalPoints += points[i][index]
        # ninjaTrain(i+1,index, totalPoints)
        # totalPoints -= points[i][index]

        ninjaTrain(i+1,index, totalPoints + points[i][index])
  
  ninjaTrain(0,-1,0)
  return maxPoints

# Recursion - Optimal one[Follow this!]
def ninjaTraining(points):
  def ninjaTrain(i,j):
    if i >= len(points):
      return 0
    
    maxPoints = float('-inf')
    for index in range(len(points[i])):
      if index != j:
        point = points[i][index] + ninjaTrain(i+1,index)
        maxPoints = max(maxPoints, point)
    return maxPoints
  
  return ninjaTrain(0,-1)

# Memoization (Top-Bottom DP)
def ninjaTraining(points):
  dp = [[-1]*len(points[0]) for _ in range(len(points))]

  def ninjaTrain(i,j):
    if i >= len(points):
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    maxPoints = float('-inf')
    for index in range(len(points[i])):
      if index != j:
        point = points[i][index] + ninjaTrain(i+1,index)
        maxPoints = max(maxPoints, point)
    dp[i][j] = maxPoints
    return dp[i][j]
  
  return ninjaTrain(0,-1)

# Steps to convert memoization to tabulation
# 1. write the base case - same as memoization
# 2. write all possible states in terms of for loop
# 3. when recursion is called, change it to dp array and when or if cost[arr], use that. recursion is for already solved problem so, we use dp arr
# 4. copy the recursion and write

# Some Hints
# Always avoid for loop in 2d or 1d DP
# instead write 2 recursion calls

# Tabulation (Bottom-Top DP)
# let i be days and j be tasks(3 tasks)
# we will also use a last task varible here to track last task(called index as in prev recursion)
# Tabulation is pretty easy here, after computing base cases
# for f(i,j) in recursion -> make them into loops(days loop from 1 -> n-1(for i) and last task loop from 0 to 2(for j) inside that do the same as recursive method)
# Here we return max(dp[0]) because for last index, we exclude and see other two. values for each dp[n-1] will vary
def ninjaTraining(points):
  dp = [[-1]*len(points[0]) for _ in range(len(points))]
  n = len(points)
  # Base cases
  dp[n-1][0] = points[n-1][0]
  dp[n-1][1] = points[n-1][1]
  dp[n-1][2] = points[n-1][2]

  for days in range(n-2,-1,-1):
    for last_task in range(3):
      # From here on, code is exactly same as recursion but I am changing names for understanding properly(Here it's starting from front instead of back)
      for task in range(len(points[days])):
        if task != last_task:
          point = points[days][task] + dp[days+1][task]
          dp[days][last_task] = max(dp[days][last_task], point)

  print(dp)
  return max(dp[0])

print(ninjaTraining([[10,40,70],[20,50,80],[30,60,90]]))

# Ninja Training - Tabulation Approach:
# Goal: Maximize total points over N days without repeating the same task on consecutive days.

# 1. Create a DP table: dp[day][last_task] to store max points till 'day' if last task was 'last_task'.
#    last_task = 0,1,2 for tasks, and 3 means no task restriction (used only at base).
# 2. Base case (day 0):
#    For each last_task in 0,1,2, set dp[0][last_task] = max(points[0][task]) for task != last_task
# 3. Loop from day 1 to N-1:
#    For each possible last_task:
#        Try all tasks that are not equal to last_task.
#        For each valid task:
#            dp[day][last_task] = max(dp[day][last_task], points[day][task] + dp[day-1][task])
# 4. Final answer is max(dp[N-1]) — i.e., best score on last day regardless of last task used.

    





      

