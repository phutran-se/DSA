"""
DSALinkedList.py - A doubly linked list implementation

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

# DSAListNode class
class DSAListNode:
    def __init__(self, value):
        self.value = value      # Value of the node
        self.prev = None        # Reference to the previous node
        self.next = None        # Reference to the next node

# DSALinkedList class
class DSALinkedList:
    def __init__(self):
        self.head = None        # Reference to the first node
        self.tail = None        # Reference to the last node
    
    # Function to check if the list is empty
    def is_empty(self):
        return self.head == None        # Check if the head is None
    
    # Function to insert a new node at the beginning
    def insert_first(self, value):
        new_node = DSAListNode(value)   # Create a new node
        if self.is_empty():             # If the list is empty, set the head and tail to the new node
            self.head = self.tail = new_node
        else:                           # Otherwise, set the new node as the head and link it to the previous head
            new_node.next = self.head   # Set the next of the new node to the current head
            self.head.prev = new_node   # Set the previous of the current head to the new node
            self.head = new_node        # Set the head to the new node
    
    # Function to insert a new node at the end of the list
    def insert_last(self, value):       
        new_node = DSAListNode(value)   # Create a new node
        if self.is_empty():             # If the list is empty, set the head and tail to the new node
            self.head = self.tail = new_node
        else:                           # Otherwise, set the new node as the tail and link it to the previous tail
            new_node.prev = self.tail   # Set the previous of the new node to the current tail
            self.tail.next = new_node   # Set the next of the current tail to the new node
            self.tail = new_node        # Set the tail to the new node
    
    # Function to remove the first node
    def remove_first(self):             
        if self.is_empty():             # If the list is empty, raise an exception
            raise Exception("List is empty") # Raise an exception
        value = self.head.value
        if self.head == self.tail:      # If the head is the same as the tail, set both to None
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Set the head to the next node
            self.head.prev = None       # Set the previous of the new head to None
        return value
    
    # Function to remove the last node
    def remove_last(self): 
        if self.is_empty(): 
            raise Exception("List is empty")
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value
    
    # Function to peek the first node
    def peek_first(self):
        if self.is_empty():     # If the list is empty, raise an exception
            raise Exception("List is empty")
        return self.head.value  # Return the value of the head
    
    # Peek the last node
    def peek_last(self):  
        if self.is_empty():     # If the list is empty, raise an exception
            raise Exception("List is empty")
        return self.tail.value  # Return the value of the tail
    
    # Function to display the list
    def display(self):
        curr = self.head            # Start from the head
        vals = []                   # List to store the values
        while curr:                 # Iterate through the list (if not None)
            vals.append(curr.value) # Append the value to the list
            curr = curr.next        # Move to the next node
        return vals                 # Return the list of values
    
    # Function to display the list as string
    def __str__(self):
        return str(self.display())
