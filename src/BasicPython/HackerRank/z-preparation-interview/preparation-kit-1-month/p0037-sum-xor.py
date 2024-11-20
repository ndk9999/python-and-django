#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    one = 0
    bit = 0
    m = n
    
    while m > 0:
        m = m & (m-1)
        one += 1
        
    m = n
    while m > 0:
        m = m >> 1
        bit += 1
    
    return 1 << (bit - one)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
