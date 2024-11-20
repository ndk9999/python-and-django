#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

mod = 10**9 + 7

def legoBlocks(n, m):
    if n < 1 or m < 1:
        return 0
        
    if n == 1:
        return 0 if m > 4 else 1

    perms = [0, 1, 2, 4, 8]

    for i in range(5, m + 1):
        perms.append((perms[i-1] + perms[i-2] + perms[i-3] + perms[i-4]) % mod)

    wall_n = [pow(p, n, mod) for p in perms]
    valid_n = [0, 1]
    
    for k in range(2, m + 1):
        sum_gp = sum(valid_n[i] * wall_n[k - i] for i in range(1, k)) % mod
        valid_n.append((wall_n[k] - sum_gp) % mod)

    return valid_n[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
