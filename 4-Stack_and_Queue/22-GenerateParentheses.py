# Recursion (Refer to backtracking, dp series before this problem)
# Parentheses is valid if open >= closed brackets. we can add closed bracket if open > closed at any point
# we can keep on adding open brackets on long as it's < n. if open == closed == n: then it's finished, append it to the result
# We keep a stack outside to collect all brackets, to remove brackets from one rec call to other rec call. we do stack pop after a recursion call
# Draw a decision tree to understand this problem
# This problem is easy if you know recursion very well

# https://neetcode.io/solutions/generate-parentheses (7:57 for decision tree, refer it)
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []
        def generateP(open, closed):
            if open == closed == n:
                return result.append("".join(stack))
            
            if open < n:
                stack.append("(")
                generateP(open+1, closed)
                stack.pop()
            
            if open > closed:
                stack.append(")")
                generateP(open, closed+1)
                stack.pop()
        
        generateP(0,0)
        return result

if __name__ == "__main__":
  s = Solution()
  print(s.generateParenthesis(3))