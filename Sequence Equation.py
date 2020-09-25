#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    q = []
    r = []
    for x in range(1,len(p)+1):
        for i, y in enumerate(p):
            if x == y:
                q.append(i+1)
    for e in q:
        for i, y in enumerate(p):
            if e == y:
                r.append(i+1)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
