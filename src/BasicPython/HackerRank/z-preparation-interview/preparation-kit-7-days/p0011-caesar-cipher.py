#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    if k == 0:
        return s
    
    hoa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    thuong = 'abcdefghijklmnopqrstuvwxyz'
    n = len(hoa)
    r = ''
    
    for c in s:
        if c >= 'A' and c <= 'Z':
            idx = hoa.index(c)
            r += hoa[(idx + k) % n]
        elif c >= 'a' and c <= 'z':
            idx = thuong.index(c)
            r += thuong[(idx + k) % n]
        else:
            r += c
            
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
