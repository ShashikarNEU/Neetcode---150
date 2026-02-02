class Queue():
    def __init__(self,k:'int'):
        self._a = [None]*k 
        self._MAX = k
        ## YOU CAN HAVE YOUR PRIVATE DATA MEMBER HERE
        self._front = 0
        self._rear = -1
        self._size = 0
            
    def enQueue(self, T)->'bool':
        if not self.isFull():
            self._rear = (self._rear + 1) % self._MAX
            self._a[self._rear] = T
            self._size += 1
            return True
        return False
        
    def deQueue(self)->'int':
        if not self.isEmpty():
            num = self._a[self._front]
            self._front = (self._front + 1) % self._MAX
            self._size -= 1
            return num
        return None
                        
    def isEmpty(self):
        return self._size == 0
    
    def isFull(self):
        return self._size == self._MAX
         
    def Front(self)->'int':
        if not self.isEmpty():
            return self._a[self._front]
        return None
    
    def Rear(self) -> 'int':
        if not self.isEmpty():
            return self._a[self._rear]
        return None
        
    def __str__(self)->'str':
        if self.isEmpty():
            return "Queue is empty"
        s = []
        count = self._front
        for _ in range(self._size):  
            s.append(str(self._a[count]))
            count = (count + 1) % self._MAX
 
        return " ".join(s)
         
    def __len__(self)->'int':
        return self._size

## Implement stack using queue
class StackUsingQueue():
    def __init__(self, n=10): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY QUEUE THAY YOU WROTE
        self._q = Queue(n)
        self._MAX = n
    
    def push(self, x: int) -> None:
        if not self._q.isFull():
            self._q.enQueue(x)
        
    def pop(self) -> int:
        q2 = Queue(self._MAX)

        while len(self._q) > 1:
            num = self._q.deQueue()
            q2.enQueue(num)

        x = self._q.deQueue()

        while not q2.isEmpty():
            num = q2.deQueue()
            self._q.enQueue(num)
        
        return x
    
    def __len__(self):
        print(self._q)

    def top(self) -> int:
        return self._q.Rear()
        
    def empty(self) -> bool:
        if self._q.isEmpty():
            return True
        return False

# Main function to test Queue
if __name__ == "__main__":
    q = Queue(5)

    print(q.enQueue(10))  # True
    print(q.enQueue(20))  # True
    print(q.enQueue(30))  # True
    print(q.enQueue(40))  # True
    print(q.enQueue(50))  # True
    print(q.enQueue(60))  # False (Queue full)

    print("Queue:", q)  # 10 -> 20 -> 30 -> 40 -> 50
    print("Front:", q.Front())  # 10
    print("Rear:", q.Rear())  # 50

    print(q.deQueue())  # True
    print("Queue after deQueue:", q)  # 20 -> 30 -> 40 -> 50

    print(q.enQueue(60))  # True
    print("Queue after enQueue 60:", q)  # 20 -> 30 -> 40 -> 50 -> 60
    print(q.isFull())  # True
    print(q.isEmpty())  # False
    
    print("----------------------------")
    s1 = StackUsingQueue()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    x = s1.pop()
    print(x)

    