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
    while found == -1 and lowerBound <= higherBound: 
        meanIndex = (lowerBound + higherBound)//2 # Get the mean index
        if A[meanIndex] < needle: 
            lowerBound = meanIndex + 1 # Target must be in the upper half
        elif A[meanIndex] > needle: 
            higherBound = meanIndex - 1 # Target must be in the lower half 
        else: 
            found = meanIndex # Found our target
    return found

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
    while isSorted and i < (lenA-1):
        isSorted = False            # Assume the list is sorted  
        for j in range(lenA-i-1):
            if A[j] > A[j+1]: 
                A[j],A[j+1]=A[j+1],A[j] # Swap elements
                isSorted = True # A swap occurred, so the list is not yet sorted
        i +=1
            

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
        while (j > 0) and A[j] < A[j-1]: 
            A[j] = A[j-1]   # Shift elements to the right
            j -=1
        A[j] = current # Insert the current element at its correct position 

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
        A[i], A[minIdx] = A[minIdx],A[i] # Swap the smallest element with A[i]

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...




