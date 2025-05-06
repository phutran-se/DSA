#
# Data Structures and Algorithms COMP5008
#
# Python file to hold all sorting methods
#
# 

'''
DSAsorts.py - sorting methods

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
'''

import random

# ============== BINARY SEARCH ==============
def binSearch(A, needle):
    """  
    Performs binary search to find the index of 'needle' in a sorted list A.  
    Returns the index if found, otherwise returns -1.  

    Args:  
        A (list): A sorted list of elements.  
        needle (any): The element to search for.  

    Returns:  
        int: The index of 'needle' in A, or -1 if not found.  
    """  
    found = -1
    lowerBound = 0
    higherBound = len(A)-1
    while (found == -1) and (lowerBound <= higherBound): 
        meanIndex = (lowerBound + higherBound)//2 # Get the mean index
        if A[meanIndex] < needle: 
            lowerBound = meanIndex + 1 # Target must be in the upper half
        elif A[meanIndex] > needle: 
            higherBound = meanIndex - 1 # Target must be in the lower half 
        else: 
            found = meanIndex # Found our target
    return found

# ============== BUBBLE SORT ==============
def bubbleSort(A):
    """  
    Sorts a list A in ascending order using the Bubble Sort algorithm.  
    Optimized with an early exit if the list is already sorted.  

    Args:  
        A (list): The list to be sorted.  
    """  
    lenA = len(A)
    isSorted = True # Flag for optimization
    i = 0 
    while isSorted and i < (lenA - 1):
        isSorted = False            # Assume the list is sorted  
        for j in range(lenA - i - 1):
            if A[j] > A[j+1]: 
                A[j], A[j+1] = A[j+1], A[j] # Swap elements
                isSorted = True # A swap occurred, so the list is not yet sorted
        i +=1
            
# ============== INSERTION SORT ==============
def insertionSort(A):
    """  
    Sorts a list A in ascending order using the Insertion Sort algorithm.  

    Args:  
        A (list): The list to be sorted.  
    """  
    lenA = len(A)
    for i in range(1, lenA):
        current = A[i]
        j = i
        while (j > 0) and (A[j-1] > current): 
            A[j] = A[j-1]   # Shift elements to the right
            j -= 1
        A[j] = current # Insert the current element at its correct position 

# ============== SELECTION SORT ==============
def selectionSort(A):
    """  
    Sorts a list A in ascending order using the Selection Sort algorithm.  

    Args:  
        A (list): The list to be sorted.  
    """  
    lenA = len(A)
    for i in range(lenA): 
        minIdx = i # Assume the minimum element is at index i 
        for j in range(i, lenA):
            if A[j] < A[minIdx]:
                minIdx = j # Update minIdx if a smaller element is found 
        A[i], A[minIdx] = A[minIdx], A[i] # Swap the smallest element with A[i]

# ============== MERGE SORT ==============
def mergeSort(A):
    """ 
    mergeSort - front-end for kick-starting the recursive algorithm
    Args:
        A (list): Array to be sorted
    """
    if A is not None and len(A) > 1:
        mergeSortRecurse(A, 0, len(A) - 1)

def mergeSortRecurse(A, leftIdx, rightIdx):
    """ 
    mergeSortRecurse - recursive implementation of MergeSort
    Args:
        A (list): Array to be sorted
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
    """
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)  # Sort left half
        mergeSortRecurse(A, midIdx + 1, rightIdx)  # Sort right half
        merge(A, leftIdx, midIdx, rightIdx)  # Merge sorted halves

def merge(A, leftIdx, midIdx, rightIdx):
    """ 
    merge - merges two sorted subarrays into a single sorted array
    Args:
        A (list): Array containing the subarrays
        leftIdx (int): Starting index of the left subarray
        midIdx (int): Ending index of the left subarray
        rightIdx (int): Ending index of the right subarray
    """
    tempArr = [0] * (rightIdx - leftIdx + 1)
    i = leftIdx  # Index for left subarray
    j = midIdx + 1  # Index for right subarray
    k = 0  # Index for temp array

    # Merge two subarrays into tempArr
    while i <= midIdx and j <= rightIdx:
        if A[i] <= A[j]:  # Use <= for stable sort
            tempArr[k] = A[i]
            i += 1
        else:
            tempArr[k] = A[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    while i <= midIdx:
        tempArr[k] = A[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j <= rightIdx:
        tempArr[k] = A[j]
        j += 1
        k += 1

    # Copy tempArr back to original array
    for k in range(len(tempArr)):
        A[leftIdx + k] = tempArr[k]

# ============== QUICK SORT ==============
def quickSort(A):
    """ 
    quickSort - front-end for kick-starting the recursive algorithm with left-most pivot
    Args:
        A (list): Array to be sorted
    """
    if A is not None and len(A) > 1:
        quickSortRecurse(A, 0, len(A) - 1)

def quickSortRecurse(A, leftIdx, rightIdx):
    """ quickSortRecurse - recursive implementation of QuickSort with left-most pivot
    Args:
        A (list): Array to be sorted
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
    """
    if leftIdx < rightIdx:
        pivotIdx = leftIdx  # Left-most pivot
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        # Sort left partition, ensure no infinite recursion
        if newPivotIdx - 1 > leftIdx:
            quickSortRecurse(A, leftIdx, newPivotIdx - 1)
        # Sort right partition, ensure no infinite recursion
        if newPivotIdx + 1 < rightIdx:
            quickSortRecurse(A, newPivotIdx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    """ 
    doPartitioning - partitions the array around the pivot
    Args:
        A (list): Array to be partitioned
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
        pivotIdx (int): Index of the pivot
    Returns:
        int: New index of the pivot after partitioning
    """
    pivotVal = A[pivotIdx]
    # Move pivot to end
    A[pivotIdx], A[rightIdx] = A[rightIdx], pivotVal
    currIdx = leftIdx

    # Partition array
    for i in range(leftIdx, rightIdx):
        if A[i] < pivotVal:
            A[i], A[currIdx] = A[currIdx], A[i]
            currIdx += 1

    # Move pivot to its final position
    A[rightIdx], A[currIdx] = A[currIdx], pivotVal
    return currIdx

def quickSortMedian3(A):
    """ 
    quickSortMedian3 - front-end for QuickSort with median-of-three pivot
    Args:
        A (list): Array to be sorted
    """
    if A is not None and len(A) > 1:
        quickSortMedian3Recurse(A, 0, len(A) - 1)

def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    """ 
    quickSortMedian3Recurse - recursive QuickSort with median-of-three pivot
    Args:
        A (list): Array to be sorted
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
    """
    if leftIdx < rightIdx:
        pivotIdx = getMedianOfThree(A, leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        if newPivotIdx - 1 > leftIdx:
            quickSortMedian3Recurse(A, leftIdx, newPivotIdx - 1)
        if newPivotIdx + 1 < rightIdx:
            quickSortMedian3Recurse(A, newPivotIdx + 1, rightIdx)

def getMedianOfThree(A, leftIdx, rightIdx):
    """ 
    getMedianOfThree - selects the median of the first, middle, and last elements as pivot
    Args:
        A (list): Array to select pivot from
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
    Returns:
        int: Index of the median element
    """
    midIdx = (leftIdx + rightIdx) // 2
    # Sort left, mid, right to find median
    if A[leftIdx] > A[midIdx]:
        A[leftIdx], A[midIdx] = A[midIdx], A[leftIdx]
    if A[leftIdx] > A[rightIdx]:
        A[leftIdx], A[rightIdx] = A[rightIdx], A[leftIdx]
    if A[midIdx] > A[rightIdx]:
        A[midIdx], A[rightIdx] = A[rightIdx], A[midIdx]
    return midIdx  # Middle element is the median

def quickSortRandom(A):
    """ 
    quickSortRandom - front-end for QuickSort with random pivot
    Args:
        A (list): Array to be sorted
    """
    if A is not None and len(A) > 1:
        quickSortRandomRecurse(A, 0, len(A) - 1)

def quickSortRandomRecurse(A, leftIdx, rightIdx):
    """ 
    quickSortRandomRecurse - recursive QuickSort with random pivot
    Args:
        A (list): Array to be sorted
        leftIdx (int): Starting index of the subarray
        rightIdx (int): Ending index of the subarray
    """
    if leftIdx < rightIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)  # Random pivot
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        if newPivotIdx - 1 > leftIdx:
            quickSortRandomRecurse(A, leftIdx, newPivotIdx - 1)
        if newPivotIdx + 1 < rightIdx:
            quickSortRandomRecurse(A, newPivotIdx + 1, rightIdx)