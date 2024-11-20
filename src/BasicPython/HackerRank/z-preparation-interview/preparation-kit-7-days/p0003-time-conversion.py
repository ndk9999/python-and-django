#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    idx = len(s) - 2
    b = s[idx:]
    h, m, k = map(int, s[:idx].split(':'))
    if b == 'PM':
        if h < 12:
            h += 12
    elif h == 12:
            h = 0
        
    return f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(k).zfill(2)}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
