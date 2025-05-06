import random
import DSAsorts
from Funct import *

def generate_random_array(size=10, min_val=1, max_val=100):
    # Create array with random integers
    arr = [random.randint(min_val, max_val) for _ in range(size)]
    return arr


def test_merge_sort():
    print_info("\n*** MERGE SORT ***")
    print_info2("=== Testing MergeSort ===")
    # Generate random array
    arr = generate_random_array()
    print("> Before sorting:", arr)
    # Call MergeSort
    DSAsorts.mergeSort(arr)
    print("> After sorting:", arr)

def test_quick_sort():
    print_info("\n*** QUICK SORT ***")
    print_info2("=== Testing QuickSort (Left-Most Pivot) ===")
    # Generate random array
    arr1 = generate_random_array()
    print("> Before sorting:", arr1)
    # Call QuickSort (left-most pivot)
    DSAsorts.quickSort(arr1)
    print("> After sorting:", arr1)

    print_info2("\n=== Testing QuickSortMedian3 ===")
    # Generate new random array
    arr2 = generate_random_array()
    print("> Before sorting:", arr2)
    # Call QuickSortMedian3
    DSAsorts.quickSortMedian3(arr2)
    print("> After sorting:", arr2)

    print_info2("\n=== Testing QuickSortRandom ===")
    # Generate new random array
    arr3 = generate_random_array()
    print("> Before sorting:", arr3)
    # Call QuickSortRandom
    DSAsorts.quickSortRandom(arr3)
    print("> After sorting:", arr3)
    print()

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)

    # Run tests
    test_merge_sort()
    test_quick_sort()