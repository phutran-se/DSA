"""
DSAQueue.py - Implement the Queue data structure with Shuffling and Circular Queue

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

import numpy as np

# Implement the DSAQueue class
class DSAQueue:
    def __init__(self, capacity=100):
        self.queue = np.empty(shape=capacity, dtype=object)  # Initialize the queue with a list of None values
        self.front = 0                  # Initialize the front of the queue
        self.rear = 0                   # Initialize the rear of the queue
        self.count = 0                  # Initialize the count of the queue
        self.capacity = capacity        # Initialize the capacity of the queue
    
    def is_empty(self):
        return self.count == 0          # If the count is 0, the queue is empty
    
    def is_full(self):
        return self.count == self.capacity # If the count is equal to the capacity, the queue is full
    
    def enqueue(self, item):
        # Implement the enqueue method in the subclasses
        raise NotImplementedError("Subclasses must implement enqueue()")
    
    def dequeue(self):
        # Implement the dequeue method in the subclasses
        raise NotImplementedError("Subclasses must implement dequeue()")
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")   # Raise an exception if the queue is empty
        return self.queue[self.front]           # Return the item at the front of the queue (without removing it)
    
    
# Implement the ShufflingQueue class that inherits from DSAQueue
class ShufflingQueue(DSAQueue):
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item # Add the item to the rear of the queue
        self.rear += 1               # Increment the rear
        self.count += 1              # Increment the count
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")   # Raise an exception if the queue is empty
        item = self.queue[0]                    # Get the item at the front of the queue
        for i in range(1, self.count):          # Shift the items in the queue to the left
            self.queue[i-1] = self.queue[i]
        self.queue[self.count-1] = None         # Remove the item at the rear of the queue
        self.count -= 1                         # Decrement the count
        self.rear = self.count                  # Adjust rear correctly after shifting
        return item
    def __str__(self):
        return str(self.queue[:self.count])
    
# Implement the CircularQueue class that inherits from DSAQueue
class CircularQueue(DSAQueue):
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item                # Add the item to the rear of the queue
        self.rear = (self.rear + 1) % self.capacity # Increment the rear
        self.count += 1                             # Increment the count
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")           # Raise an exception if the queue is empty
        item = self.queue[self.front]                   # Get the item at the front of the queue
        self.queue[self.front] = None                   # Remove the item from the queue
        self.front = (self.front + 1) % self.capacity   # Increment the front
        self.count -= 1                                 # Decrement the count
        return item

    def __str__(self):
        parts = ""                                      # Initialize the parts
        index = self.front                              # Start from the front
        for _ in range(self.count):                     # Loop through the queue
            parts += " " + str(self.queue[index])       # Add the item to the parts
            index = (index + 1) % self.capacity         # Move to the next item
        return str(parts)