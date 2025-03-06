#!/bin/sh 

# This shell script runs 5 case (array size in 100, 1000, 5000, 10000 and 20000)
# Array can be Ascending (a), Descending (d), Random (r) and Nearly Sorted (n)
# Run these cases with 3 algorthms: Bubble Sort, Insertion Sort and Selection Sort

for size in 100 1000 5000 10000 20000; do
    for type in a d r n; do
        python3 SortsTestHarness2.py $size $type
    done
done