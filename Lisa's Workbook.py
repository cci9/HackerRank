#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    count = 0
    page = 0
    for i in range(n):
        j = 0
        page_chapterwise = 0
        while j <= arr[i] - 1:
            if j + k <= arr[i]:
                j = j + k
                page = page + 1
                page_chapterwise = page_chapterwise + 1
            else:
                j = j + arr[i] % k
                page = page + 1
                page_chapterwise = page_chapterwise + 1
            prob = j
            if page == 1:
                for problem in range(1, prob + 1):
                    if problem == page:
                        count = count + 1
            else:
                for problem in range((k * (page_chapterwise - 1) + 1), prob + 1):
                    if problem == page:
                        count = count + 1
    return count




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
