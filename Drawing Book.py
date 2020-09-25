#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    count = 0
    if p <= (n - p):
        if p == 1:
            return (count)
        else:
            a = 0
            b = 1
            while count <= p:
                count = count + 1
                a = a + 2
                b = b + 2
                if a == p or b == p:
                    return (count)
                    break
    if p > (n - p):
        if n % 2 == 0:
            if p == n:
                return (count)
            else:
                a = n
                b = n + 1
                while count <= n:
                    count = count + 1
                    a = a - 2
                    b = b - 2
                    if a == p or b == p:
                        return (count)
                        break
        else:
            if p == n or p == n - 1:
                return (count)
            else:
                a = n
                b = n - 1
                while count <= n:
                    count = count + 1
                    a = a - 2
                    b = b - 2
                    if a == p or b == p:
                        return (count)
                        break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
