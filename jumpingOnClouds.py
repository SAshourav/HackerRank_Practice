#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. INTEGER k
#

def jumpingOnClouds(c, k):
    n = len(c) # length of cloud array
    energy = 100 # initial energy
    current_index = 0 # start at index 0
    # Keep jumping until we return to index 0
    while True:
        # Jump k steps, use modulo to wrap around for circular array
        current_index = (current_index + k) % n # modulo n keeps index in [0, n-1]
        # Lose 1 energy for the jump
        energy = energy - 1
        # If landing on thunderhead cloud (c[current_index] == 1), lose 2 more energy
        if c[current_index] == 1:
            energy = energy - 2
        # If back at index 0, stop
        if current_index == 0:
            break
    output = energy # store final energy
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()
