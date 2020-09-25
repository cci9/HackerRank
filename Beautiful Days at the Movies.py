#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for num in range(i, j + 1):
        num_str = str(num)
        num_lst = list(num_str)
        num_lst.reverse()
        num_rev = 0
        for i in range(len(num_lst)):
            num_rev1 = int(num_lst[i])
            num_rev = num_rev + num_rev1 * (10 ** (len(num_lst) - 1 - i))
        if abs(num - num_rev) % k == 0:
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
