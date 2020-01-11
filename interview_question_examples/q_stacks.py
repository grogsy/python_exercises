# Implement a queue using two stacks

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self, value):
        self.s1.append(value)
        
    def deque(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
    
    def peek(self):
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[0]
