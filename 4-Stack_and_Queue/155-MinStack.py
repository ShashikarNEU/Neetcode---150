# Use two stacks - one normal and one min stack, min stack should have the min elements 
# so, keep checking when pushing into the stack. when poping, check the min stack also for that element, it should be on the top
# if it's not there, leave it. pop element was never in min stack
# Take a simple example and do it
class MinStack:
    def __init__(self):
        self._stack = []
        self._minStack = []
        
    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._minStack) == 0:
            self._minStack.append(val)
        else:
            if self.top() <= self._minStack[-1]:
                self._minStack.append(self.top())
                    
    def pop(self) -> None:
        if not self.isEmpty():
            if self.top() == self._minStack[-1]:
                self._minStack.pop()
            self._stack.pop()
        
    def top(self) -> int:
        if not self.isEmpty():
            return self._stack[-1]

    def isEmpty(self):
        return len(self._stack) == 0
        
    def getMin(self) -> int:
        if len(self._minStack) != 0:
            return self._minStack[-1]
        
