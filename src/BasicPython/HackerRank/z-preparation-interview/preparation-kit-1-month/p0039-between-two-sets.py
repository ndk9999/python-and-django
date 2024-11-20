#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def ucln(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def bcnn(x, y):
    return x * y // ucln(x, y)

def getTotalX(a, b):
    # Write your code here
    bc = a[0]
    uc = b[0]
    
    for k in a:
        bc = bcnn(bc, k)
        
    for k in b:
        uc = ucln(uc, k)
    
    count = 0
    k = 1
    while bc * k <= uc:
        if uc % (bc * k) == 0:
            count += 1
        k += 1
    
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
