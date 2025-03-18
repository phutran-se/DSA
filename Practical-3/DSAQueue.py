"""
DSAQueue.py - Implement the Queue data structure with Shuffling and Circular Queue

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

# Implement the DSAQueue class
class DSAQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0
        self.capacity = capacity
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.capacity
    
    def enqueue(self, item):
        raise NotImplementedError("Subclasses must implement enqueue()")
    
    def dequeue(self):
        raise NotImplementedError("Subclasses must implement dequeue()")
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

# Implement the ShufflingQueue class that inherits from DSAQueue
class ShufflingQueue(DSAQueue):
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear += 1
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[0]
        for i in range(1, self.count):
            self.queue[i-1] = self.queue[i]
        self.queue[self.count-1] = None
        self.rear -= 1
        self.count -= 1
        return item

# Implement the CircularQueue class that inherits from DSAQueue
class CircularQueue(DSAQueue):
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item

