class Stack():
    def __init__(self): 
        self._a = []
        self._maxspace = 0
        
    def isFull(self):
        return False  
        
    def isEmpty(self):
        return len(self._a) == 0
        
    def push(self, num):
        self._a.append(num)
        self._maxspace = max(self._maxspace, len(self._a))
            
    def pop(self):
        if not self.isEmpty():
            return self._a.pop()
        return None
    
    def top(self):
        if not self.isEmpty():
            return self._a[-1]
        return None
            
    def __len__(self):
        return len(self._a)
    
    def space(self):
        return self._maxspace

## Implement queue using stack
class QueueUsingStack():
    def __init__(self): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY STACK THAT YOU WROTE
        self._s = Stack()
    
    def push(self, x: int) -> None:
        self._s.push(x)
        
    def pop(self) -> int:
        s1 = Stack()

        while not self._s.isEmpty():
            num = self._s.pop()
            s1.push(num)

        popElement = s1.pop()
        #print("s1 stack: ",s1._a)
        
        while not s1.isEmpty():
            num = s1.pop()
            self._s.push(num)
        #print("s stack: ",s._a)
    
        return popElement
    
    def peek(self) -> int:
        s1 = Stack()

        while not self._s.isEmpty():
            num = self._s.pop()
            s1.push(num)

        popElement = s1.top()
        #print("s1 stack: ",s1._a)
        
        while not s1.isEmpty():
            num = s1.pop()
            self._s.push(num)
        #print("s stack: ",s._a)
    
        return popElement
        
    def empty(self) -> bool:
        return self._s.isEmpty()

# Main function to test the Stack
if __name__ == "__main__":
    s = Stack()
    
    print("Is stack empty?", s.isEmpty())  # True
    s.push(10)
    s.push(20)
    s.push(30)
    
    print("Stack top:", s.top())  # 30
    print("Stack length:", len(s))  # 3
    
    print("Popped element:", s.pop())  # 30
    print("Stack top after pop:", s.top())  # 20
    print("Stack length after pop:", len(s))  # 2
    
    print("Stack space used:", s.space())  # 3 (Max space reached)

    s.pop()
    s.pop()
    print("Is stack empty?", s.isEmpty())  # True
    print("-----------------Queue Using Stack-----------------------")
    q = QueueUsingStack()

    print("Queue is empty:", q.empty())  # Expected: True

    q.push(1)
    q.push(2)
    q.push(3)

    print("Front element (peek):", q.peek())  # Expected: 1

    print("Popped:", q.pop())  # Expected: 1
    #print(q._s._a)
    print("Popped:", q.pop())  # Expected: 2

    print("Queue is empty:", q.empty())  # Expected: False

    q.push(4)
    print("Front element (peek):", q.peek())  # Expected: 3

    print("Popped:", q.pop())  # Expected: 3
    print("Popped:", q.pop())  # Expected: 4

    print("Queue is empty:", q.empty())  # Expected: True