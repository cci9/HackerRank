#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    z = [0, 0, 0, 0, 0]
    for e in arr:
        if e == 1:
            z[0] = z[0] + 1
        if e == 2:
            z[1] = z[1] + 1
        if e == 3:
            z[2] = z[2] + 1
        if e == 4:
            z[3] = z[3] + 1
        if e == 5:
            z[4] = z[4] + 1
    return (z.index(max(z)) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
