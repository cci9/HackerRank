#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    count = 0
    while i <= (len(c)-2):
        if i + 2 == len(c):
            count = count + 1
            break
        if c[i + 2] == 0:
            #m.append((c[i + 2]))
            count = count + 1
            i = i + 2
        else:
            #m.append((c[i + 1]))
            count = count + 1
            i = i + 1
        if i == len(c):
            break
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
