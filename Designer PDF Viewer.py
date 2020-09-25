#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    m =[]
    for i, e in enumerate(word):
        for i, code in enumerate(range(ord('a'), ord('z') + 1)):
            if chr(code) == e:
                m.append(h[i])
    return (max(m) * len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
