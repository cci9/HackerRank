#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ar =[]
    for s_num in range(p, q + 1):
        s_str = str(s_num)
        s_sq_num = s_num * s_num
        s_sq_str = str(s_sq_num)
        s_sq_list = list(s_sq_str)
        left_s_squqre_list = []
        right_s_squqre_list = []
        for i, e in enumerate(s_sq_list):
            if i < (len(s_sq_list) - len(s_str)):
                left_s_squqre_list.append(e)
            else:
                right_s_squqre_list.append(e)
        left_sum = 0
        for i, e in enumerate(left_s_squqre_list):
            e = int(e)
            e = e * (10 ** (len(left_s_squqre_list) - i - 1))
            left_sum = left_sum + e
        right_sum = 0
        for i, e in enumerate(right_s_squqre_list):
            e = int(e)
            e = e * (10 ** (len(right_s_squqre_list) - i - 1))
            right_sum = right_sum + e
        s_sq_sum = left_sum + right_sum
        if s_sq_sum == s_num:
            ar.append(s_num)
            print(s_num, end = ' ')
    if len(ar) == 0:
        print('INVALID RANGE')




if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
