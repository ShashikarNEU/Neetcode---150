# https://neetcode.io/solutions/longest-palindromic-substring
# Brute Force
# List all substrings and do plaindrome fn on each of them
# that's n^3 time
# for i in range(n):
#   for j in range(j,n):
#     if palindrome(s[i:j+1]): count length

# For optimal time, we can do n^2 time
# iterate through every letter of the strings and use a two pointer appoarch(we can do end-end 2 pointer(start from end and converge towards one point) or same place 2 pointer(expand from one place and go to the end))
# same place 2 pointer makes sense here. so, use that. start from a letter and if letter(i) == letter(j) then, do i-=1,j+=1
# This will give us odd length palindromes. For even length palindromes, start from i,i+1 and expand using 2 pointer(same algo as odd)
# This optimal algo time is n2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        result = "" # Contains longest palindromic substring
        for i in range(len(s)):
            left, right = i, i
            # Odd Length
            while right < len(s) and left >= 0 and s[left] == s[right]:
                palindrome_substring_length = right-left+1
                if palindrome_substring_length > maxLength:
                    result = (s[left:right+1])
                    maxLength = right-left+1
                left-=1
                right+=1
            
            # Even Length
            left, right = i, i+1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                palindrome_substring_length = right-left+1
                if palindrome_substring_length > maxLength:
                    result = (s[left:right+1])
                    maxLength = right-left+1
                left-=1
                right+=1
        #print(result)
        return result

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("abbd"))