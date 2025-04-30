"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

import csv
import numpy as np
from DSAHeap import DSAHeap, DSAHeapEntry, heap_sort
from Funct import print_error, print_info, print_info2

def read_and_sort_csv(filename, limit=7000):
    """Read priority-name pairs from a CSV file and sort them using HeapSort."""
    # Initialize NumPy array with size limit
    heap_array = np.array([None] * limit, dtype=object)
    count = 0
    
    # Read CSV file
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensure row has priority and name
                    try:
                        priority = int(row[0])  # First column as priority
                        name = row[1]  # Second column as value
                        if count >= len(heap_array):
                            # Resize array by doubling its size
                            heap_array = np.resize(heap_array, len(heap_array) * 2)
                        heap_array[count] = DSAHeapEntry(priority, name)
                        count += 1
                    except ValueError:
                        print_error(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print_error(f"File {filename} not found")
        return []
    
    # Apply HeapSort on the used portion of the array
    sorted_array = heap_sort(heap_array, count)
    return sorted_array

def sort_numbers(numbers):
    """Sort a list of numbers in ascending order using HeapSort."""
    # Convert list of numbers to NumPy array of DSAHeapEntry
    heap_array = np.array([None] * len(numbers), dtype=object)
    for i, num in enumerate(numbers):
        heap_array[i] = DSAHeapEntry(num, num)  # Priority and value are the same
    
    # Apply HeapSort (produces descending order due to Max Heap)
    sorted_array = heap_sort(heap_array, len(numbers))
    
    # Extract sorted numbers
    sorted_numbers = [entry.get_value() for entry in sorted_array]
    return sorted_numbers

def test_heap1():
    print_info("\n==== Test DSAHeap (1) =====")
    heap = DSAHeap(10)
    heap.add(4, 4)
    heap.add(10, 10)
    heap.add(3, 3)
    heap.add(5, 5)
    heap.add(1, 1)
    
    print_info("Heap contents:")
    heap.display()
    
    print_info("\nRemoving highest priority:")
    entry = heap.remove()
    print_info(f"Removed: Priority={entry.get_priority()}, Value={entry.get_value()}")
    
    print_info("\nHeap after removal:")
    heap.display()

def test_heap2():
    print_info2("\n==== Test DSAHeap (2) =====")
    heap = DSAHeap(10)
    heap.add(120, "David")
    heap.add(110, "Wilson")
    heap.add(300, "Matt")
    
    print_info("Heap contents:")
    heap.display()
    
    print_info("\nRemoving highest priority:")
    entry = heap.remove()
    print_info(f"Removed: Priority={entry.get_priority()}, Value={entry.get_value()}")
    
    print_info("\nHeap after removal:")
    heap.display()

def test_heap_sort_numbers():
    print_info2("\n==== Test Heap Sort (Numbers) =====")
    test_cases = [
        ([5, 2, 9, 1, 7], "Random numbers"),
        ([1], "Single element"),
        ([3, 3, 3], "Duplicate elements"),
        ([10, 5, 8, 12, 3], "More random numbers"),
        ([], "Empty list")
    ]
    
    for numbers, description in test_cases:
        print_info(f"\nTest case: {description}")
        sorted_numbers = sort_numbers(numbers)
        print_info(f"Input: {numbers}")
        print_info(f"Sorted: {sorted_numbers}")

def test_heap_sort():
    print_info2("\n==== Test Heap Sort (CSV) =====")
    print_info("Sorting CSV file (first 20 entries for brevity):")
    sorted_array = read_and_sort_csv("RandomNames7000.csv", limit=7000)
    for entry in sorted_array[:20]:  # Show first 20 sorted entries
        print_info(f"Priority={entry.get_priority()}, Value={entry.get_value()}")

if __name__ == "__main__":
    # Test heap implementation
    try:
        test_heap1()
        test_heap2()
    except Exception as e:
        print_error(f'> [ERROR] heap: {e}')
    
    # Test HeapSort with numbers
    try:
        test_heap_sort_numbers()
    except Exception as e:
        print_error(f'> [ERROR] heap_sort_numbers: {e}')
    
    # Test HeapSort with CSV
    try:
        test_heap_sort()
    except Exception as e:
        print_error(f'> [ERROR] heap_sort_csv: {e}')