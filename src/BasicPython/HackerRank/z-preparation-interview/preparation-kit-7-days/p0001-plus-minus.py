#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    
    for k in arr:
        if k == 0:
            zero += 1
        elif k > 0:
            pos += 1
        else:
            neg += 1
            
    print("%0.6f" % (pos / len(arr)))
    print("%0.6f" % (neg / len(arr)))
    print("%0.6f" % (zero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
