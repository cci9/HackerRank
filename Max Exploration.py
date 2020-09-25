#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count = 0
    i = 0
    while i <= len(s):
        if s[i:i+3] != 'SOS':
            a = s[i:i+3]
            for j in range(len(a)):
                if j == 0 or j == 2:
                    if a[j] != 'S':
                        count = count + 1
                if j == 1:
                    if a[j] != 'O':
                        count = count + 1
        else:
            pass
        i = i + 3
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
