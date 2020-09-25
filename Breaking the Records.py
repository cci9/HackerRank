#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    count_best = 0
    count_worst = 0
    for e in scores:
        if e > best:
            best = e
            count_best = count_best + 1
        if e < worst:
            worst = e
            count_worst = count_worst + 1
    return (count_best, count_worst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
