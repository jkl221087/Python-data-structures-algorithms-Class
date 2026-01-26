class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self): 
        return self.stack1[-1]
    
    def is_empty(self):
        return len(self.stack1) == 0
        
    def enqueue (self, values):
        while not self.is_empty() and self.peek() < values:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(values)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

q = MyQueue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
