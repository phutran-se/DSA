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
    """
    Max Heap implementation using an array-based approach.
    """
    def __init__(self, capacity=10000):
        """
        Initialize an empty heap with given capacity.
        """
        self._heap = np.array([None] * capacity, dtype=object)
        self._count = 0

    def add(self, priority, value):
        """
        Add a new entry to the heap and maintain the max-heap property.
        """
        if self._count >= len(self._heap):
            raise ValueError("Heap is full")

        # Add new entry at the end
        self._heap[self._count] = DSAHeapEntry(priority, value)
        self._count += 1

        # Move it up to correct position
        self._trickle_up(self._count - 1)

    def remove(self):
        """
        Remove and return the highest priority (root) entry.
        """
        if self._count == 0:
            raise ValueError("Heap is empty")

        # Store root to return
        result = self._heap[0]

        # Move last element to root
        self._heap[0] = self._heap[self._count - 1]
        self._count -= 1

        # Restore heap property
        if self._count > 0:
            self._trickle_down(0)

        return result

    def _trickle_up(self, index):
        """
        Move the element at index up to its correct position.
        """
        parent_idx = (index - 1) // 2
        while index > 0 and self._heap[index].get_priority() > self._heap[parent_idx].get_priority():
            self._heap[index], self._heap[parent_idx] = self._heap[parent_idx], self._heap[index]
            index = parent_idx
            parent_idx = (index - 1) // 2

    def _trickle_down(self, index):
        """
        Move the element at index down to its correct position.
        """
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < self._count and self._heap[left].get_priority() > self._heap[largest].get_priority():
                largest = left

            if right < self._count and self._heap[right].get_priority() > self._heap[largest].get_priority():
                largest = right

            if largest != index:
                self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
                index = largest
            else:
                break

    def display(self):
        """
        Display all entries in the heap.
        """
        for i in range(self._count):
            entry = self._heap[i]
            print(f"Index {i}: Priority={entry.get_priority()}, Value={entry.get_value()}")


def heapify(heap_array, num_items):
    """
    Convert an array into a max-heap.
    """
    for i in range(num_items // 2 - 1, -1, -1):
        index = i
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < num_items and heap_array[left].get_priority() > heap_array[largest].get_priority():
                largest = left

            if right < num_items and heap_array[right].get_priority() > heap_array[largest].get_priority():
                largest = right

            if largest != index:
                heap_array[index], heap_array[largest] = heap_array[largest], heap_array[index]
                index = largest
            else:
                break


def heap_sort(array, num_items):
    """
    Sort an array of DSAHeapEntry objects in ascending order using HeapSort.
    """
    # Step 1: Build a max-heap
    heapify(array, num_items)

    # Step 2: Repeatedly move the largest element (root) to the end
    for end in range(num_items - 1, 0, -1):
        # Swap the root with the current last element
        array[0], array[end] = array[end], array[0]

        # Trickle down the new root in the reduced heap
        curr_idx = 0
        heap_size = end

        while True:
            left = 2 * curr_idx + 1
            right = 2 * curr_idx + 2
            largest = curr_idx

            if left < heap_size and array[left].get_priority() > array[largest].get_priority():
                largest = left

            if right < heap_size and array[right].get_priority() > array[largest].get_priority():
                largest = right

            if largest != curr_idx:
                array[curr_idx], array[largest] = array[largest], array[curr_idx]
                curr_idx = largest
            else:
                break

    return array
