import numpy as np

class DSAHeapEntry:
    """
    Class to store a priority-value pair for the heap.
    """
    def __init__(self, priority, value):
        self._priority = priority
        self._value = value

    def get_priority(self):
        """
        Return the priority of the entry.
        """
        return self._priority

    def set_priority(self, priority):
        """
        Set the priority of the entry.
        """
        self._priority = priority

    def get_value(self):
        """
        Return the value of the entry.
        """
        return self._value

    def set_value(self, value):
        """
        Set the value of the entry.
        """
        self._value = value

class DSAHeap:
    """Max Heap implementation using an array-based approach."""
    def __init__(self, capacity=10000):
        """Initialize an empty heap with given capacity."""
        self._heap = np.array([None] * capacity, dtype=object)
        self._count = 0

    def add(self, priority, value):
        """
        Add a new entry to the heap and maintain heap property.
        """
        if self._count >= len(self._heap):
            raise ValueError("Heap is full")
        
        # Add at the end
        self._heap[self._count] = DSAHeapEntry(priority, value)
        self._count += 1
        # Trickle up to restore heap property
        self._trickle_up(self._count - 1)

    def remove(self):
        """
        Remove and return the highest priority entry.
        """
        if self._count == 0:
            raise ValueError("Heap is empty")
        
        # Store root to return
        result = self._heap[0]
        # Move last element to root
        self._heap[0] = self._heap[self._count - 1]
        self._count -= 1
        # Trickle down to restore heap property
        if self._count > 0:
            self._trickle_down(0)
        
        return result

    def _trickle_up(self, index):
        """
        Trickle up the element at index to restore heap property.
        """
        parent_idx = (index - 1) // 2
        
        while index > 0 and self._heap[index].get_priority() > self._heap[parent_idx].get_priority():
            # Swap with parent
            self._heap[index], self._heap[parent_idx] = self._heap[parent_idx], self._heap[index]
            index = parent_idx
            parent_idx = (index - 1) // 2

    def _trickle_down(self, index):
        """
        Trickle down the element at index to restore heap property.
        """
        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2
        largest_idx = index

        # Check if left child exists and is larger
        if left_child_idx < self._count and self._heap[left_child_idx].get_priority() > self._heap[largest_idx].get_priority():
            largest_idx = left_child_idx
        
        # Check if right child exists and is larger
        if right_child_idx < self._count and self._heap[right_child_idx].get_priority() > self._heap[largest_idx].get_priority():
            largest_idx = right_child_idx
        
        # If largest is not the current index, swap and continue
        if largest_idx != index:
            self._heap[index], self._heap[largest_idx] = self._heap[largest_idx], self._heap[index]
            self._trickle_down(largest_idx)

    def display(self):
        """
        Display the heap entries.
        """
        for i in range(self._count):
            entry = self._heap[i]
            print(f"Index {i}: Priority={entry.get_priority()}, Value={entry.get_value()}")

def heapify(heap_array, num_items):
    """
    Convert an array into a max heap.
    """
    # Start from last non-leaf node
    for i in range(num_items // 2 - 1, -1, -1):
        # Trickle down to place element in correct position
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        largest_idx = i

        if left_child_idx < num_items and heap_array[left_child_idx].get_priority() > heap_array[largest_idx].get_priority():
            largest_idx = left_child_idx
        
        if right_child_idx < num_items and heap_array[right_child_idx].get_priority() > heap_array[largest_idx].get_priority():
            largest_idx = right_child_idx
        
        if largest_idx != i:
            heap_array[i], heap_array[largest_idx] = heap_array[largest_idx], heap_array[i]
            # Recursively trickle down
            left_child_idx = 2 * largest_idx + 1
            right_child_idx = 2 * largest_idx + 2
            while left_child_idx < num_items:
                largest_idx = left_child_idx
                if right_child_idx < num_items and heap_array[right_child_idx].get_priority() > heap_array[left_child_idx].get_priority():
                    largest_idx = right_child_idx
                if heap_array[largest_idx].get_priority() <= heap_array[i].get_priority():
                    break
                heap_array[largest_idx], heap_array[i] = heap_array[i], heap_array[largest_idx]
                left_child_idx = 2 * largest_idx + 1
                right_child_idx = 2 * largest_idx + 2

def heap_sort(array, num_items):
    """
    Sort an array of DSAHeapEntry objects using HeapSort (ascending order).
    """
    # Heapify the array (creates a max-heap)
    heapify(array, num_items)
    
    # Extract elements one by one
    for i in range(num_items - 1, -1, -1):
        # Swap root with the last element
        array[0], array[i] = array[i], array[0]
        # Reduce heap size
        num_items -= 1
        # Trickle down to restore heap property
        curr_idx = 0
        while True:
            left_child_idx = 2 * curr_idx + 1
            right_child_idx = 2 * curr_idx + 2
            largest_idx = curr_idx

            # Check left child
            if left_child_idx < num_items and array[left_child_idx].get_priority() > array[largest_idx].get_priority():
                largest_idx = left_child_idx
            
            # Check right child
            if right_child_idx < num_items and array[right_child_idx].get_priority() > array[largest_idx].get_priority():
                largest_idx = right_child_idx
            
            # If largest is not current, swap and continue
            if largest_idx != curr_idx:
                array[curr_idx], array[largest_idx] = array[largest_idx], array[curr_idx]
                curr_idx = largest_idx
            else:
                break
    
    return array