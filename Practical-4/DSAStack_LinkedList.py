"""
DSAStack_LinkedList.py - A stack implementation using a linked list

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSALinkedList import DSALinkedList

class DSAStack_LinkedList:
    def __init__(self):
        self.stack = DSALinkedList()
    
    def is_empty(self):
        return self.stack.is_empty()
    
    def push(self, value):
        self.stack.insert_first(value)
    
    def pop(self):
        return self.stack.remove_first()
    
    def peek(self):
        return self.stack.peek_first()
    
    def display(self):
        return self.stack.display()
    
    def __str__(self):
        return self.stack.display()
