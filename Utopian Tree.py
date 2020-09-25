#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    ini = 1
    if n == 0:
        pass
    else:
        for i in range(1,n+1):
            if i % 2 != 0:
                ini = ini * 2
            if i % 2 == 0:
                ini = ini + 1
    return ini

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
