"""
DSAQueue_LinkedList.py - A queue implementation using a linked list

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSALinkedList import DSALinkedList

class DSAQueue_LinkedList:
    def __init__(self):
        self.queue = DSALinkedList()
    
    def is_empty(self):
        return self.queue.is_empty()
    
    def enqueue(self, value):
        self.queue.insert_last(value)
    
    def dequeue(self):
        return self.queue.remove_first()
    
    def peek(self):
        return self.queue.peek_first()
    
    def display(self):
        return self.queue.display()
    
    def __str__(self):
        return self.queue.display()
