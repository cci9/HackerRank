#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    like = 0
    shared = 5
    cumulative = 0
    i = 1
    while i <= n:
        like = shared//2
        cumulative = like + cumulative
        shared = like * 3
        i += 1
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
