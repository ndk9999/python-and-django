#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    if n == 1:
        return 'Richard'
        
    turn = 0
    while True:
        p = int(math.log2(n))
        m = 1 << p
        if n == m:
            n = n // 2
        else:
            n = n - m
        if n == 1:
            break
        turn = 1 - turn
        
    return 'Louise' if turn == 0 else 'Richard'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
