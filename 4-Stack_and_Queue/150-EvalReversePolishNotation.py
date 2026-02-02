#  Easy question - idk why it's meduim
#  push non operand into stack, if operand pop it eval it and push it into stack and
#  repeat this till every element is covered in input arr
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operand = {'+','-','*','/'}
        for token in tokens:
            if token not in operand:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
        return int(stack[-1])

            