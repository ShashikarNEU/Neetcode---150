# LOGIC
# After thinkng for a while, you will realize that we can tranverse s1 and s2 by i,j while comparing with s3
# To keep track of the s3 index, we can use i+j. (0 at start but when we have i, second index and j 4th index. s3 will be at 6th index(i+j))[THINK]
# Termination codn - when i == len(s1) and j == len(s2) and i+j == len(s3) return True
# i+j == len(s3) is required beacuse we also need to reach s3 end, if s3 has still a letter left unmatched then, it's wrong
# return False in that case
# basic recusion - 
# 1.when i index of s1 is same i+j index of s3, go to rec(i+1,j) call
# 2.when j index of s1 is same i+j index of s3, go to rec(i,j+1) call

# IMP stuff -> keep track of the indexes to make sure they don't go out of bounds. 
# when i is out of bounds and j in bounds, it will give error. so, handle it
# same for when j is out of bounds
# this can also happen when i+j is out of bounds(s3 string is very short) so, do i+j < len(s3) also in rec call

# Recursion
from collections import defaultdict


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n+m != len(s3):
            return False
        
        def backtrack(i,j):
            if i == n and j == m:
                return True
            
            if i < n and s1[i] == s3[i+j]:
                if backtrack(i+1,j):
                    return True
            
            if j < m and s2[j] == s3[i+j]:
                if backtrack(i,j+1):
                    return True
            
            return False
        
        return backtrack(0,0)

def first_occurence(s):
    hashTable = defaultdict(int)
    for string in s:
        if string in hashTable:
            hashTable[string] += 1
        else:
            hashTable[string] = 1
    
    for index,string in enumerate(s):
        if hashTable[string] == 1:
            return index
    
    return -1


# https://neetcode.io/solutions/interleaving-string
# Alternative soln - add k paramater for s3 and for memo and tab, treat it as 2d DP
# Neetcode soln
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True
            
            return False
        
        return dfs(0, 0, 0)


# Memoization DP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        dp = [[None]*(m+1) for _ in range(n+1)]

        if n+m != len(s3):
            return False
        
        def backtrack(i,j):
            if i == n and j == m:
                return True
            
            if dp[i][j] != None:
                return dp[i][j]

            if i < n and s1[i] == s3[i+j]:
                if backtrack(i+1,j):
                    dp[i][j] = True
                    return dp[i][j]
            
            if j < m and s2[j] == s3[i+j]:
                if backtrack(i,j+1):
                    dp[i][j] = True
                    return dp[i][j]
            
            dp[i][j] = False
            return dp[i][j]
        
        return backtrack(0,0)

# Tabulation DP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        dp = [[None]*(m+1) for _ in range(n+1)]
        
        if n+m != len(s3):
            return False

        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i == n and j == m:
                    dp[i][j] = True
                    continue
                
                if i < n and s1[i] == s3[i+j]:
                    if dp[i+1][j]:
                        dp[i][j] = True
                        continue

                if j < m and s2[j] == s3[i+j]:
                    if dp[i][j+1]:
                        dp[i][j] = True
                        continue
            
                dp[i][j] = False
                
 
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(s.isInterleave("", "", ""))
    print(s.isInterleave("ab", "bc", "abbce"))
    print(s.isInterleave("a", "b", "a"))
    