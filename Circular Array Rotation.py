#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    output = [0] * len(a)  # Initialize output array with same length as a
    if k > len(a):
        k = k % len(a)  # Reduce k to effective rotations
    if k <= len(a):  # Handle all cases (including k == len(a))
        for i in range(len(a)):
            # Place element at index i to its new position after k rotations
            new_index = (i + k) % len(a) # new array er rotation er pore je index ase sei index e amra original array er value gula serial wise rakhtechi
            output[new_index] = a[i]
    
    # Process queries
    result = []
    for q in queries:
        result.append(output[q])
    
    return result
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
