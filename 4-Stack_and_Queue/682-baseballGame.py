class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        operands = {'C','D','+'}
        for i in range(len(operations)):
            if operations[i] not in operands:
                stack.append(int(operations[i]))
            elif operations[i] == 'C' and stack:
                stack.pop()
            elif operations[i] == 'D' and stack:
                stack.append(2*stack[-1])
            elif operations[i] == '+' and len(stack)>1:
                stack.append(stack[-1]+stack[-2])
        
        return sum(stack)



        