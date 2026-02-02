# https://neetcode.io/solutions/palindrome-partitioning
# For this question, we use backtracking
# we take loop from 0 to n, till i for a particular str, if it's a palindrome, append it. for length after i (j+1)
# Do recursive call again for the same. base case is to return and append if i > len(s)

# for eg- [aab] first loop takes a, aa, aab then it checks for palindrome with part strings then, for rest of the str, ab for a, b for aa, [] for aab(This does not happen cuz aab not palindrome). for aa, recursion repeats the same again. Termination cdn for this is when index >= length of str. return and append to part. When backtracking, pop the string from part because it's already added to result

class Solution:
    def palindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
                
    def partition(self, s: str) -> list[list[str]]:
        result = []
        partition = []

        def palindrome_part(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    palindrome_part(j+1)
                    partition.pop()
        
        palindrome_part(0)

        return result
          
if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))