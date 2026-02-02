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

# Way to appoarch this by thinking
# You will think where to put the start pointers- from the end, from the start or one from the end and other from the start?
# palindrome str can be anywhere so, you will have to consider all whose possibilities
# run a for loop along s and for each i, run palindrome starting from i(As a mid point)

# But longest palindrome can be odd or even so, you will have to consider both

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_string = ""
        max_length = float('-inf')
        for i in range(n):
            # Odd Length Palindrome
            start, end = i,i
            while start >= 0 and end <= n-1 and s[start]==s[end]:
                length = end-start+1
                if length > max_length:
                    max_length = length
                    max_string = s[start:end+1]

                start-=1
                end+=1
            
            # Even Length Palindrome
            start, end = i,i+1
            while start >= 0 and end <= n-1 and s[start]==s[end]:
                length = end-start+1
                if length > max_length:
                    max_length = length
                    max_string = s[start:end+1]

                start-=1
                end+=1
        
        return max_string

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("abbd"))