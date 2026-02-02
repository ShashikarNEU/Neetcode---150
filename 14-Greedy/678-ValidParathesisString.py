# Similar to recursion logic
# Have a varaible for checking (,),*
# if ( -> +1, ) -> -1, * -> do everything

# since there is *, have two variables leftMin, leftMax
# increment and decrement min,max when facing (,)
# but when facing *, leftMax+=1, leftMin-=1
# if leftMax < 0 return False
# if leftMin == 0 at the end return True (leftMin will be 0 when brackets are balanced)

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = leftMin = 0

        for bracket in s:
            if bracket == '(':
                leftMax+=1
                leftMin+=1
            elif bracket == ')':
                leftMax-=1
                leftMin-=1
            else:
                leftMax+=1
                leftMin-=1
            
            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
        
        if leftMin == 0:
            return True
        
        return False

# Backtracking - Brure Force(DP)
# TC = 3^n, SC = n (call stack space)
class Solution:
    def checkValidString(self, s: str) -> bool:
        def backtrack(i, open):
            if open < 0:
                return False
            if i==len(s) and open == 0:
                return True
            if i == len(s):
                return False
            
            if s[i] == '(':
                return backtrack(i+1, open+1)
            
            if s[i] == ')':
                return backtrack(i+1, open-1)

            if s[i] == '*':
                 return backtrack(i+1, open+1) or backtrack(i+1, open-1) or backtrack(i+1, open)
        
        return backtrack(0,0)

# Memoization
# TC= n2, SC = n2
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1]*(n+1) for i in range(n+1)]
        def backtrack(i, open):
            if open < 0:
                return False
            if i==len(s) and open == 0:
                return True
            if i == len(s):
                return False
            
            if dp[i][open] != -1:
                return dp[i][open]
            
            if s[i] == '(':
                dp[i][open] = backtrack(i+1, open+1)
            
            if s[i] == ')':
                dp[i][open] = backtrack(i+1, open-1)

            if s[i] == '*':
                 dp[i][open] = backtrack(i+1, open+1) or backtrack(i+1, open-1) or backtrack(i+1, open)
            
            return dp[i][open]
        
        return backtrack(0,0)

        