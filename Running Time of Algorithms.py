#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                a = arr[i]
                arr.pop(i)
                arr.insert(j, a)
                count = count + i - j
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
