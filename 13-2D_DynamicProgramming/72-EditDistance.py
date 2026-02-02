# https://neetcode.io/solutions/edit-distance
# This is a tricky problem
# for insert, delete and replace, we don't have to do it and not do it(6 rec calls)
# we can just simulate it using indexes
# for insert, if we insert a j letter to word1 before i's index then, i's index will be same, j will be incremented toj+1(cuz j will same as i-1)
# for delete, if we delete in word1, i will be incremented(i+1) but j will be same
# for replace, if we replace the char of word2 in word1 then both indexes will be same so, increament both (i+1, j+1)
# during recursion, if we both are same, then (i+1,j+1)

# Termination codns
# if word2 is empty and word1 is non empty, then, we have to delete remaining chars in word1 to make it equal to word2. (m-i)
# if word2 is non empty and word1 is empty, then, we have to add remaining chars in word1 to make it equal to word2. (n-j)
# if both are empty, 0 operations are required

# HINT:- for insert, new charcters comes at i-1 so, word1[i-1]==word2[j] (internally) so, it's backtrack(i,j+1)

# Recursion
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        def backtrack(i,j):
            if j == n and i == m:
                return 0
            
            # delete remaining word1 characters
            if j == n and i != m:
                return (m-i)
            
            # insert remaining word2 characters
            if j != n and i == m:
                return (n-j)
            
            # equal
            # This is already the min so, we can just return it
            if word1[i] == word2[j]:
                return backtrack(i+1,j+1)
            
            # Not equal
            # insert
            insert = 1 + backtrack(i,j+1)

            # delete
            delete = 1 + backtrack(i+1,j)

            # replace
            replace = 1 + backtrack(i+1,j+1)
            
            return min(insert, delete, replace)
        
        return backtrack(0,0)

# Memoization DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        def backtrack(i,j):
            if j == n and i == m:
                return 0
            
            # delete remaining word1 characters
            if j == n and i != m:
                return (m-i)
            
            # insert remaining word2 characters
            if j != n and i == m:
                return (n-j)
            
            if dp[i][j] != -1:
                return dp[i][j]

            # equal
            # This is already the min so, we can just return it
            if word1[i] == word2[j]:
                dp[i][j] = backtrack(i+1,j+1)
                return dp[i][j]
            
            # Not equal
            # insert
            insert = 1 + backtrack(i,j+1)

            # delete
            delete = 1 + backtrack(i+1,j)

            # replace
            replace = 1 + backtrack(i+1,j+1)
            
            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        
        return backtrack(0,0)

# Tabulation DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[-1]*(n+1) for _ in range(m+1)]

        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if j == n and i == m:
                    dp[i][j] = 0
                    continue
            
                # delete remaining word1 characters
                if j == n and i != m:
                    dp[i][j] = m-i
                    continue
                
                # insert remaining word2 characters
                if j != n and i == m:
                    dp[i][j] = n-j
                    continue
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                    continue
            
                # Not equal
                # insert
                insert = 1 + dp[i][j+1]

                # delete
                delete = 1 + dp[i+1][j]

                # replace
                replace = 1 + dp[i+1][j+1]
                
                dp[i][j] = min(insert, delete, replace)
        
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse","ros"))
    print(s.minDistance("intention","execution"))
    
    