#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = 0
    for i, e in enumerate(bill):
        if i != k:
            s = s + e
    s = s / 2
    if b > s:
        print(int(b-s))
    else:
        print('Bon Appetit')

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
