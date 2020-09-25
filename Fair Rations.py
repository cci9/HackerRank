#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    if len(B) == 1:
        if B[0] % 2 == 0:
            count = count + 1
            return count
    if len(B) == 2:
        if B[0] % 2 == 0 and B[1] % 2 == 0:
            return 0
        elif B[0] % 2 != 0 and B[1] % 2 != 0:
            return 2
        else:
            return 'NO'
    else:
        for i in range(len(B)):
            if B[i] % 2 != 0:
                if i == len(B) - 1:
                    return 'NO'
                else:
                    B[i] = B[i] + 1
                    B[i + 1] = B[i + 1] + 1
                    count = count + 2
            even_check = 0
            for j in range(len(B)):
                if B[j] % 2 != 0:
                    even_check = even_check + 1
            if even_check == 0:
                break
            else:
                continue
        possibility = 0
        for j in range(len(B)):
            if B[j] % 2 != 0:
                possibility = possibility + 1
        if possibility > 0:
            return 'NO'
        else:
            return count
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
