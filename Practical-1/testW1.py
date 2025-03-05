'''
testW1.py - some tests for week 1

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
'''

from DSAsorts import * 

A = [8, 1, 0, 7, 2, 3, 9, 4, 6, 11, 10, 5]
print("Original: ", A)
#bubbleSort(A)
insertionSort(A)
#selectionSort(A)
print("Sorted: ", A)
print("----")
B=[20, 8, 7]
for b in B: 
    idx = binSearch(A, b)
    if idx == -1: 
        print(f"{b} not found in A")
    else:
        print(f"{b} found at {idx} in A")


# Some test case
"""
# Bubble Sort
python3 SortsTestHarness.py 10 ba
python3 SortsTestHarness.py 10 bd
python3 SortsTestHarness.py 10 br
python3 SortsTestHarness.py 10 bn

# Selection Sort
python3 SortsTestHarness.py 10 sa
python3 SortsTestHarness.py 10 sd
python3 SortsTestHarness.py 10 sr
python3 SortsTestHarness.py 10 sn

# Insertion Sort
python3 SortsTestHarness.py 10 ia
python3 SortsTestHarness.py 10 id
python3 SortsTestHarness.py 10 ir
python3 SortsTestHarness.py 10 in
"""