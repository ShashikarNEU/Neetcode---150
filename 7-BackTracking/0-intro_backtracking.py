# TIP for mutiple rcursion calls, don't visualize it by one by one
# Try using the recursion tree to visualize it. 
# one recursion call has to be fully finished before starting the next one

# Part 1 - https://www.youtube.com/watch?v=kvRjNm4rVBE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=5
# Part 1- Fib fn
def fib(n):
  if n <= 1:
    return n
  return fib(n-1)+fib(n-2)

def fib_otherWay(n):
  if n <= 1:
    return n
  n1 = fib_otherWay(n-1)
  n2 = fib_otherWay(n-2)
  return n1 + n2

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

# Time Complexity
# for n numbers, for each n -> 2 calls are made and there are n numbers -> 2 * 2 * 2 ...n times = 2^n
# O(2^n) for recursion in this case

# Part 2 - Printing all subsequences(https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6)
# subsequence -> contingous/non-contingous array seq which follows the order of the arr
# f = [3,1,2]
# {}
# 3
# 1
# 2
# 3 1
# 1 2
# 3 2 (not contingous but follows the order so, subsequence)
# 3 1 2

# We can print all the subsequences using the power set algo
# but we will be using recursion to print subsequence
# Refer Printing_all_subsequences.png for the recursion tree

# Logic -> For each index, we pick it or we don't, do that for n indexes -> 2* .. n times = 2^n * n(print each seq)
# SC = n At worst, recursion stack space will be n(Usually it will be 3-> see diagram)
# In one index -> do add, recursion call and remove, recursion call. When index >= length: print and return

def print_all_subquences(index, res, arr, n):
  if index >= n:
    print(res)
    return
  res.append(arr[index])
  print_all_subquences(index+1, res, arr, n)
  res.remove(arr[index])
  print_all_subquences(index+1, res, arr, n)


from PIL import Image
# Call the test function
if __name__ == "__main__":
  n = 3
  arr = [3, 1, 2]
  print_all_subquences(0, [], arr, n)





