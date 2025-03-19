"""
Test.py - Tests for DSALinkedList, DSAStack_LinkedList, DSAQueue_LinkedList classes

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAStack_LinkedList import DSAStack_LinkedList
from DSAQueue_LinkedList import DSAQueue_LinkedList
from DSALinkedList import DSALinkedList
from Funct import print_info, print_error

# Test DSALinkedList
def test_dsa_linked_list():
    print("Testing DSALinkedList...")
    linked_list = DSALinkedList()
    
    # Test is_empty
    assert linked_list.is_empty() == True, "Test is_empty() failed"
    
    # Test insert_first
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    linked_list.insert_first(3)
    assert linked_list.head.value == 3, "Test insert_first() failed"
    
    # Test insert_last
    linked_list.insert_last(4)
    linked_list.insert_last(5)
    linked_list.insert_last(6)
    assert linked_list.tail.value == 6, "Test insert_last() failed"
    
    # Test remove_first
    assert linked_list.remove_first() == 3, "Test remove_first() failed"
    assert linked_list.head.value == 2, "Test remove_first() failed"
    
    # Test remove_last
    assert linked_list.remove_last() == 6, "Test remove_last() failed"
    assert linked_list.tail.value == 5, "Test remove_last() failed"
    
    # Test peek_first
    assert linked_list.peek_first() == 2, "Test peek_first() failed"
    
    # Test peek_last
    assert linked_list.peek_last() == 5, "Test peek_last() failed"
    
    print_info("All tests passed for DSALinkedList!\n")


# Test DSAStack_LinkedList
def test_dsa_stack_linked_list():
    print("Testing DSAStack_LinkedList...")
    stack = DSAStack_LinkedList()
    
    # Test is_empty
    assert stack.is_empty() == True, "Test is_empty() failed"
    
    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.stack.head.value == 3, "Test push() failed"
    
    # Test pop
    assert stack.pop() == 3, "Test pop() failed"
    assert stack.stack.head.value == 2, "Test pop() failed"
    
    # Test peek
    assert stack.peek() == 2, "Test peek() failed"
    
    print_info("All tests passed for DSAStack_LinkedList!\n")

# Test DSAQueue_LinkedList
def test_dsa_queue_linked_list():
    print("Testing DSAQueue_LinkedList...")
    queue = DSAQueue_LinkedList()
    
    # Test is_empty
    assert queue.is_empty() == True, "Test is_empty() failed"
    
    # Test enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queue.head.value == 1, "Test enqueue() failed"
    
    # Test dequeue
    assert queue.dequeue() == 1, "Test dequeue() failed"
    assert queue.queue.head.value == 2, "Test dequeue() failed"
    
    # Test peek
    assert queue.peek() == 2, "Test peek() failed"
    
    print_info("All tests passed for DSAQueue_LinkedList!\n")

# Run the test functions
test_dsa_linked_list()
test_dsa_stack_linked_list()
test_dsa_queue_linked_list()
