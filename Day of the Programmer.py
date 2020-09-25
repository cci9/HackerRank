#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            date = 256 - 244
        else:
            date = 256-243
    if year > 1918:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            date = 256 - 244
        else:
            date = 256 - 243
    if year == 1918:
        date = 256 - 230
    date = str(date)
    year = str(year)
    month = '09'
    return (date + '.' + month + '.' + year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
