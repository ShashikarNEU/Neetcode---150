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