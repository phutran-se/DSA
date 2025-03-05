#!/bin/sh 

for size in 100 1000 5000 10000 20000; do
    for type in a d r n; do
        python3 SortsTestHarness2.py $size $type
    done
done