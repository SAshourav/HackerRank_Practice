#!/bin/python3

import math
import os
import random
import re
import sys

def permutationEquation(p):
    n = len(p)
    output = [0] * n  # Initialize output array for results
    # Since p is a permutation, it maps each number to another number in 1 to n.
    # To find y for a given x, you need to work backward:
    # Find the number z where p(z) = x (this is like finding the "pre-image" of x under p).
    # Then find y where p(y) = z.
    # So, y is the number such that p(p(y)) = x.
    # Example: Input p = [4, 3, 5, 1, 2] (length n = 5).
    # This means: p(1) = 4, p(2) = 3, p(3) = 5, p(4) = 1, p(5) = 2.
    for x in range(1, n + 1):  # Loop through x from 1 to n
        # For x = 1:
        # Find z where p(z) = 1. Look at p: p(4) = 1, so z = 4.
        for i in range(n):
            if p[i] == x:
                z = i + 1  # Convert to 1-based index
                # Find y where p(y) = z = 4. Look at p: p(1) = 4, so y = 1.
                for j in range(n):
                    if p[j] == z:
                        # Check: p(p(1)) = p(4) = 1, which matches x = 1. So, y = 1 for x = 1.
                        output[x - 1] = j + 1  # Store y (1-based) in output
                        # Repeat for x = 2, 3, 4, 5 to get the full output.
                        # Output for the example: [1, 3, 5, 4, 2].
                        break
                break
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
