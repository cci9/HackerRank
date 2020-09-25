#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                a = arr[i]
                arr.pop(i)
                arr.insert(j, a)
        if i != 0:
            for k in arr:
                print(k, end=' ')
        print()

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
