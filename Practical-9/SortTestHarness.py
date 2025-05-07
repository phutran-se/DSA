#**
#** Testharness to generate various different types of arrays of integers
#** and then sort them using various sorts.
#**
#** Each sort is run REPEATS times, with the first result discarded,
#** and the last REPEATS-1 runs averaged to give the running time.
#**
#** Author of java version: Andrew Turpin (andrew@cs.curtin.edu.au)
#** Date:    August 2004
#** Modified (java): Patrick Peursum
#** Date:     Sep 2009
#** Modified (python): Valerie Maxville
#** Date:    August 2017
#** Modified (python): Hayden Richards
#** Date:    March 2018
#** Modified for Prac 9: Add support for new QuickSort variants and runtime analysis
#** Date:    April 2025

import numpy as np
import timeit
import DSAsorts
import random
import sys
from Funct import *

REPEATS = 3           # Number of times to run sorts to get mean time
NEARLY_PERCENT = 0.10 # % of items to move in nearly sorted array
RANDOM_TIMES = 100    # Number of times to randomly swap elements in array

def generateArray(n, arrayType):
    """ 
    Generate an array of size n with the specified type
    Args:
        n (int): Size of the array
        arrayType (str): Type of array ('a': ascending, 'd': descending, 'r': random, 'n': nearly sorted)
    Returns:
        list: Generated array (converted to Python list)
    """
    A = np.arange(1, n + 1, 1)  # Create NumPy array with values from 1 to n

    if arrayType == 'a':
        pass  # Already ascending
    elif arrayType == 'd':  # Convert to descending
        for i in range(n // 2):
            A[i], A[n - i - 1] = A[n - i - 1], A[i]
    elif arrayType == 'r':  # Random order
        for _ in range(RANDOM_TIMES * n):
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            A[x], A[y] = A[y], A[x]
    elif arrayType == 'n':  # Nearly sorted
        for _ in range(int(n * NEARLY_PERCENT / 2) + 1):
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            A[x], A[y] = A[y], A[x]
    else:
        raise ValueError("Unsupported array type")
    
    return A.tolist()  # Convert NumPy array to Python list

def doSort(n, sortType, arrayType):
    """ Perform the specified sort on an array of the given type
    Args:
        n (int): Size of the array
        sortType (str): Type of sort ('b', 'i', 's', 'm', 'q', '3', 'r')
        arrayType (str): Type of array ('a', 'd', 'r', 'n')
    Returns:
        float: Time taken to sort in seconds
    """
    A = generateArray(n, arrayType)
    
    startTime = timeit.default_timer()
    
    if sortType == "b":
        DSAsorts.bubbleSort(A)
    elif sortType == "s":
        DSAsorts.selectionSort(A)
    elif sortType == "i":
        DSAsorts.insertionSort(A)
    elif sortType == "m":
        DSAsorts.mergeSort(A)
    elif sortType == "q":
        DSAsorts.quickSort(A)
    elif sortType == "3":
        DSAsorts.quickSortMedian3(A)
    elif sortType == "r":
        DSAsorts.quickSortRandom(A)
    else:
        raise ValueError("Unsupported sort algorithm")
    
    endTime = timeit.default_timer()
    
    # Verify array is sorted
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            raise ValueError(f"Array not sorted by {sortType}")
    
    return endTime - startTime

def main():
    """
    Main function to test sorting algorithms and generate runtime table
    """
    sizes = [1000, 5000, 10000, 20000]  # Array sizes to test
    sortTypes = [
        ("b", "BubbleSort"),
        ("i", "InsertionSort"),
        ("s", "SelectionSort"),
        ("m", "MergeSort"),
        ("q", "QuickSort"),
        ("3", "QuickSortMedian3"),
        ("r", "QuickSortRandom")
    ]
    arrayTypes = [
        ("a", "Ascending"),
        ("d", "Descending"),
        ("r", "Random"),
        ("n", "NearlySorted")
    ]
    
    # Store results for table
    results = []
    
    print("Running sorting tests...")
    for n in sizes:
        for arrayType, arrayName in arrayTypes:
            for sortType, sortName in sortTypes:
                runningTotal = 0
                for i in range(REPEATS):
                    print_info(f"> Starting [{sortName}] + [{arrayName}] + [{n}], time: {i+1}/{REPEATS}")
                    runningTotal += doSort(n, sortType, arrayType)
                    print_info2(f"\t --> Done [{sortName}] > [{arrayName}] + [{n}], time: {i+1}/{REPEATS}\n")
                avgTime = (runningTotal / (REPEATS - 1)) * 1000  # Convert to milliseconds
                results.append((n, arrayName, sortName, avgTime))
    
    # Print and save results table
    print("\nRuntime Results (in milliseconds):")
    print("Size | Data Type | Algorithm | Time (ms)")
    print("-----|-----------|-----------|----------")
    
    with open("sorting_runtimes.txt", "w") as f:
        f.write("Size | Data Type | Algorithm | Time (ms)\n")
        f.write("-----|-----------|-----------|----------\n")
        for n, arrayName, sortName, timeMs in results:
            print(f"{n} | {arrayName} | {sortName} | {timeMs:.2f}")
            f.write(f"{n} | {arrayName} | {sortName} | {timeMs:.2f}\n")

def test_sort_by(n, sortType, arrayType):
    print_info("\n* TEST SORT BY")
    runningTotal = 0
    for _ in range(REPEATS):
        startTime = timeit.default_timer()
        doSort(n, sortType, arrayType)
        endTime = timeit.default_timer()
        runningTotal += (endTime - startTime)

    print_info2(f"> Done: sortType={sortType}, arrayType={arrayType}, n={n}, time={str(runningTotal/(REPEATS - 1))}")
    print()
    

if __name__ == "__main__":
    # set stack size
    sys.setrecursionlimit(21000)
    try:
        main()

        # test sort by
        #test_sort_by(100, 'q', 'r')
    except Exception as e:
        print_error(f"> [ERROR] exception: {e}")