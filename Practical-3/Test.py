"""
Test.py - Test for DSAStack and DSAQueue classes

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAStack import DSAStack
from DSAQueue import ShufflingQueue, CircularQueue


# Test DSAStack
def test_dsa_stack():
    print("Testing DSAStack...")
    stack = DSAStack(5)
    
    # Test is_empty
    assert stack.is_empty() == True, "Test is_empty failed"
    
    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.stack == [1, 2, 3, None, None], "Test push failed"
    
    # Test is_full
    assert stack.is_full() == False, "Test is_full failed"
    
    # Test pop
    assert stack.pop() == 3, "Test pop failed"
    assert stack.stack == [1, 2, None, None, None], "Test pop failed"
    
    # Test peek
    assert stack.peek() == 2, "Test peek failed"
    print("All tests passed for DSAStack!\n")

# Test ShufflingQueue
def test_shuffling_queue():
    print("Testing ShufflingQueue...")
    queue = ShufflingQueue(5)
    
    # Test is_empty
    assert queue.is_empty() == True, "Test is_empty failed"
    
    # Test enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queue == [1, 2, 3, None, None], "Test enqueue failed"
    
    # Test is_full
    assert queue.is_full() == False, "Test is_full failed"
    
    # Test dequeue
    assert queue.dequeue() == 1, "Test dequeue failed"
    assert queue.queue == [2, 3, None, None, None], "Test dequeue failed"
    
    # Test peek
    assert queue.peek() == 2, "Test peek failed"
    print("All tests passed for ShufflingQueue!\n")

# Test CircularQueue
def test_circular_queue():
    print("Testing CircularQueue...")
    queue = CircularQueue(5)
    
    # Test is_empty
    assert queue.is_empty() == True, "Test is_empty failed"
    
    # Test enqueue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queue == [1, 2, 3, None, None], "Test enqueue failed"
    
    # Test is_full
    assert queue.is_full() == False, "Test is_full failed"
    
    # Test dequeue
    assert queue.dequeue() == 1, "Test dequeue failed"
    assert queue.queue == [None, 2, 3, None, None], "Test dequeue failed"
    
    # Test peek
    assert queue.peek() == 2, "Test peek failed"
    print("All tests passed for CircularQueue!\n")

# Run the tests
test_dsa_stack()
test_shuffling_queue()
test_circular_queue()