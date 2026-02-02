# order of the string s does not matter. as along as it's in the wordList, it's correct

# Logic
# Appoarch is to do for loop from i to n in every recursion call, if it's in the wordset move on else return False and stop it
# when it reaches the end, return True. then return True to the top using if rec(): return True

# Now, you need to check if its in the word set before rec call not in the new rec call(after). we can't check it after, if we need to, we need start and end as parameters(dp 2d) but if we check it before(this problem becomes easy)

# Recursion
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        def wordB(index):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                if s[index:j+1] in wordSet:
                    if wordB(j+1):
                        return True
            return False
                
        return wordB(0)
  
# Memoization DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [-1]*(n+1)
        def backtrack(i):
            if i >= n:
                return True
            if dp[i] != -1:
                return dp[i]
            for j in range(i,n):
                if s[i:j+1] in wordDict:
                    if backtrack(j+1):
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]
        
        return backtrack(0)

# Tabulation DP
# when copying from memoization if there is a return statement with non value like bool. 
# After assigning bool, you need to put break[IMP]
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        wordSet = set(wordDict)
        dp[n] = True
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i:j+1] in wordSet:
                    if dp[j+1]:
                        dp[i] = True
                        break
              
        return dp[0]

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode",["leet","code"]))