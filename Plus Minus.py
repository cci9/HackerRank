#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    z = 0
    n = 0
    for i in arr:
        if i < 0:
            n = n + 1
        if i > 0:
            p = p + 1
        if i == 0:
            z = z + 1
    pf = p / len(arr)
    nf = n / len(arr)
    zf = z / len(arr)
    print('%.6f' % pf)
    print('%.6f' % nf)
    print('%.6f' % zf)
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
