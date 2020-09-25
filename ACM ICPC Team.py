#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    list = []
    for i in range(len(topic) - 1):
        sub = topic[i]
        for j in range(i + 1, len(topic)):
            sub1 = topic[j]
            count = 0
            for k in range(len(sub)):
                if sub[k] == '1' or sub1[k] == '1':
                    count = count + 1
            list.append(count)
    return (max(list), list.count(max(list)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
