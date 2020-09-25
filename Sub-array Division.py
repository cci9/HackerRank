#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    if len(s) == 1:
        if s[0] == d:
            if m == 1:
                count = 1 
    else:
        for i in range(len(s)+1-m):
            dd = s[i]
            for j in range(i+1, i+m):
                dd = dd + s[j]
            if d == dd:
                count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
