# n^2 time -> Passes 129/132 test cases
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = [] # Contains all palindromic substrings
        for i in range(len(s)):
            left, right = i, i
            # Odd Length
            while right < len(s) and left >= 0 and s[left] == s[right]:
                result.append(s[left:right+1])
                left-=1
                right+=1
            
            # Even Length
            left, right = i, i+1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                result.append(s[left:right+1])
                left-=1
                right+=1
        print(result)
        return len(result)

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aaa"))
    print(s.countSubstrings("abbd"))


# DP Approach
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1
            
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
                
        # Check for substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
                    
        return count