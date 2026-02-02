# https://neetcode.io/solutions/decode-string
# Logic
# brackets -> stack
# take a stack and put everything till ]. pop it till [, store the str and pop num also. do num*str and put it back in stack
# use string prepend. when popping, do subastr = stack.pop() + substr. new stuff gets prepended.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                # To remove [
                stack.pop()
                
                digit = ""
                # We put 'stack and' codn because in starting after num has been popped, stack will empty -> error
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                
                stack.append(int(digit)*substr)
                
        
        return "".join(stack)

if __name__ == "__main__":
  s = Solution()
  print(s.decodeString("3[a]2[bc]"))
  print(s.decodeString("3[a2[c]]"))
  print(s.decodeString("2[abc]3[cd]ef"))