# Use two stacks - one normal and one min stack, min stack should have the min elements 
# so, keep checking when pushing into the stack. when poping, check the min stack also for that element, it should be on the top
# if it's not there, leave it. pop element was never in min stack
# Take a simple example and do it
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or self.min_stack[-1] >= value:
            self.min_stack.append(value)

            
    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        
