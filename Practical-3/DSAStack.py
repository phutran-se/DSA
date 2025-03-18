"""
DSAStack.py - Implement the Stack data structure

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

class DSAStack:
    def __init__(self, capacity=100):
        self.stack = [None] * capacity          # Initialize the stack with a list of None values
        self.top = -1
        self.capacity = capacity
    
    def is_empty(self):
        return self.top == -1                   # If the top is -1, the stack is empty
    
    def is_full(self):
        return self.top == self.capacity - 1    # If the top is equal to the capacity - 1, the stack is full
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")    # Raise an exception if the stack is full
        self.top += 1                           # Increment the top
        self.stack[self.top] = item             # Assign the item to the top of the stack
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")   # Raise an exception if the stack is empty
        item = self.stack[self.top]             # Get the item at the top of the stack
        self.stack[self.top] = None             # Remove the item from the stack
        self.top -= 1                           # Decrement the top
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")   # Raise an exception if the stack is empty
        return self.stack[self.top]             # Return the item at the top of the stack (without removing it)

    def __str__(self):
        return str(self.stack[:self.top + 1])   # Return the stack as a string