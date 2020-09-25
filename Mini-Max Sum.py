#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    t = max(arr)
    mini = 0
    maxi = 0
    arr.remove(max(arr))
    for e in arr:
        mini = mini + e
    arr.append(t)
    arr.remove(min(arr))
    for e in arr:
        maxi = maxi + e
    print(mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
