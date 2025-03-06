'''
SortsTestHarness2.py - Sorting Test Cases for Performance Testing

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
'''

import numpy as np
import sys
import timeit
import DSAsorts
import random
import copy

REPEATS = 3           # Number of times to run sorts to get mean time
NEARLY_PERCENT = 0.10 # % of items to move in nearly sorted array
RANDOM_TIMES = 100    # Number of times to randomly swap elements in array

def usage():
    print(" Usage: python3 SortsTestHarness2.py n y [y ...]")
    print("        where")
    print("        n is number of integers to sort")
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")
    print("           n - 1..n nearly sorted (10% moved)")

def genArray(n, arrayType):
    """
    Generate an array based on the specified type.
    """

    A = np.arange(1, n + 1, 1)  # Create array with values from 1 to n
    
    if arrayType == 'a':
        pass  # Already ascending
    elif arrayType == 'd':  # Convert to descending
        for i in range(int(n / 2)):
            A[i], A[n - i - 1] = A[n - i - 1], A[i]
    elif arrayType == 'r':  # Random order
        for _ in range(RANDOM_TIMES * n):
            x = int(random.random() * n)
            y = int(random.random() * n)
            A[x], A[y] = A[y], A[x]
    elif arrayType == 'n':  # Nearly sorted
        for _ in range(int(n * NEARLY_PERCENT / 2 + 1)):
            x = int(random.random() * n)
            y = int(random.random() * n)
            A[x], A[y] = A[y], A[x]
    else:
        raise ValueError("Unsupported array type")
    
    return A.tolist()  # Convert to Python list for DSAsorts compatibility

def doSorts(n, arrayType):
    """
    Run all three sorts on the same array and measure runtimes.
    """
    
    # Generate one base array
    bArray = genArray(n, arrayType)
    
    # Create copies for each sort
    bubbleArray = copy.deepcopy(bArray)
    selectArray = copy.deepcopy(bArray)
    insertArray = copy.deepcopy(bArray)
    
    # Measure runtimes (in second)
    runtimes = {'b': 0.0, 'i': 0.0, 's': 0.0}
    
    for _ in range(REPEATS):
        # Bubble Sort
        bubbleCopy = copy.deepcopy(bubbleArray)
        startTime = timeit.default_timer()
        DSAsorts.bubbleSort(bubbleCopy)
        endTime = timeit.default_timer()
        runtimes['b'] += (endTime - startTime)
        
        # Insertion Sort
        insertCopy = copy.deepcopy(insertArray)
        startTime = timeit.default_timer()
        DSAsorts.insertionSort(insertCopy)
        endTime = timeit.default_timer()
        runtimes['i'] += (endTime - startTime)

        # Selection Sort
        selectCopy = copy.deepcopy(selectArray)
        startTime = timeit.default_timer()
        DSAsorts.selectionSort(selectCopy)
        endTime = timeit.default_timer()
        runtimes['s'] += (endTime - startTime)
        
    
    # Verify correctness (on final run)
    for i in range(n - 1):
        if bubbleCopy[i] > bubbleCopy[i + 1]:
            raise ValueError("Bubble Sort: Array not in order")
        if insertCopy[i] > insertCopy[i + 1]:
            raise ValueError("Insertion Sort: Array not in order")
        if selectCopy[i] > selectCopy[i + 1]:
            raise ValueError("Selection Sort: Array not in order")
    
    # Average runtimes (discard first run)
    avg_runtimes = {k: v / (REPEATS - 1) for k, v in runtimes.items()}
    return avg_runtimes

# main program
if len(sys.argv) < 3:
    usage()
else:
    n = int(sys.argv[1])
    for aa in range(2, len(sys.argv)):
        arrayType = sys.argv[aa]
        runtimes = doSorts(n, arrayType)
        for sortType, runtime in runtimes.items():
            print(f"{sortType}{arrayType} {n} {runtime:.6f}")