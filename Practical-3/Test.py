"""
Test.py - Test for DSAStack and DSAQueue classes

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAStack import DSAStack
from DSAQueue import ShufflingQueue, CircularQueue
from Funct import print_info, print_error
import numpy as np


# Test DSAStack
def test_dsa_stack():
    print("Testing class DSAStack...")
    stack = DSAStack(5)
    
    assert stack.is_empty() == True, "Test is_empty() failed"
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    expected_stack = np.empty(5, dtype=object)
    expected_stack[:3] = [1, 2, 3]
    expected_stack[3:] = None
    assert np.array_equal(stack.stack, expected_stack), "Test push() failed"
    
    assert stack.is_full() == False, "Test is_full() failed"
    
    assert stack.pop() == 3, "Test pop() failed"
    expected_stack[2] = None
    assert np.array_equal(stack.stack, expected_stack), "Test pop() state failed"
    
    assert stack.peek() == 2, "Test peek() failed"

    print("All tests passed for DSAStack!\n")

# Test ShufflingQueue
def test_shuffling_queue():
    print("Testing class ShufflingQueue...")
    queue = ShufflingQueue(5)
    
    assert queue.is_empty() == True, "Test is_empty() failed"
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected_queue = np.empty(5, dtype=object)
    expected_queue[:3] = [1, 2, 3]
    expected_queue[3:] = None
    assert np.array_equal(queue.queue, expected_queue), "Test enqueue() failed"
    
    assert queue.is_full() == False, "Test is_full() failed"
    
    assert queue.dequeue() == 1, "Test dequeue() failed"
    
    # Fix: Shift elements left manually instead of incorrect slicing
    expected_queue[0] = 2
    expected_queue[1] = 3
    expected_queue[2:] = None  # Ensure the rest of the queue is None
    assert np.array_equal(queue.queue, expected_queue), "Test dequeue() failed"
    
    assert queue.peek() == 2, "Test peek() failed"

    print("All tests passed for ShufflingQueue!\n")


# Test CircularQueue
def test_circular_queue():
    print("Testing class CircularQueue...")
    queue = CircularQueue(5)
    
    assert queue.is_empty() == True, "Test is_empty() failed"
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected_queue = np.empty(5, dtype=object)
    expected_queue[:3] = [1, 2, 3]
    expected_queue[3:] = None
    assert np.array_equal(queue.queue, expected_queue), "Test enqueue() failed"
    
    assert queue.is_full() == False, "Test is_full() failed"
    
    assert queue.dequeue() == 1, "Test dequeue() failed"
    expected_queue[0] = None
    assert np.array_equal(queue.queue, expected_queue), "Test dequeue() failed"
    
    assert queue.peek() == 2, "Test peek() failed"

    print("All tests passed for CircularQueue!\n")

# Run the tests
test_dsa_stack()
test_shuffling_queue()
test_circular_queue()