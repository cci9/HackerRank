#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    i = 0
    m = []
    for i in range(len(arr)- 1 ):
        count = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count = count + 1
        m.append(count)
    return (len(arr)-max(m))
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
