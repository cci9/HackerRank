#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    p = s
    s = list(s)
    if s[8] == 'A':
        if s[0] == '1' and s[1] == '2':
            s[0] = '0'
            s[1] = '0'
        s = "".join(s)
        return s[0:8]
    if s[8] == 'P':
        if s[0] == '1' and s[1] == '2':
            s = "".join(s)
            return s[0:8]
        else:
            p = p[0:2]
            p = int(p)
            p = p + 12
            p = str(p)
            p = list(p)
            s[0] = p[0]
            s[1] = p[1]
            s = "".join(s)
            return s[0:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
