class MyQueue:
    def __init__(self):
        self.stack1 = [2]
        self.stack2 = []

    def peek(self):
        if len(self.stack1) == 0:
            return self.stack1[-1]
        
    def enqueue (self, values):
        self.stack2.append(self.stack1.pop(self.peek()))

        for i in self.stack1:
            print(i)
        return self.stack2



my = MyQueue()
print(my.enqueue(3))