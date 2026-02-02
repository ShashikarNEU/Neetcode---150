# Doing multiply x, n times will not work
# Use Exponentiation by Squaring
# for myPow(5,8)
# The time complexity for this solution is O(log n), using a technique called "Exponentiation by Squaring".

# Base Case:
# x^0 = 1.0

# Recursive Step:
# If n is EVEN:
#   x^n = (x^(n/2))^2 

# If n is ODD:
#   x^n = x * x^(n-1) 
#   (Since n-1 is even, this becomes: x * (x^((n-1)/2))^2)

# recursion logic(my soln)
# base test cases all passed but due ** operator, big n test cases are failing
class Solution: 
    def myPow(self, x: float, n: int) -> float: 
        if n == 0: 
            return 1 
        if n < 0: 
            return (1/self.myPow(x,-n)) 
        if n%2 == 0: 
            return x**(n/2) * self.myPow(x, n/2) 
        else: 
            return x * x**((n-1)/2) * self.myPow(x, (n-1)/2)

# So, do the recursion first, multiply later
# avoid using ** operator
# Hint:- instead of doing (n-1)/2 do n//2 (it's the same due to rounding off)
# TC - Logn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            half = helper(x, n//2)

            if n%2 == 0:
                return half * half
            else:
                return x * half * half
        
        res = helper(x, abs(n))
        return res if n>=0 else 1/res
