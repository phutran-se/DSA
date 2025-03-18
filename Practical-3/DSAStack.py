"""
DSAStack.py - Implement the Stack data structure

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

class DSAStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]
