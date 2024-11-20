#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isMatched(c, k):
    return (c == '{' and k == '}') or (c == '[' and k == ']') or (c == '(' and k == ')')

def isBalanced(s):
    nx = []
    
    for c in s:
        if c == '{' or c == '[' or c == '(':
            nx.append(c)
        elif len(nx) == 0:
            return 'NO'
        elif isMatched(nx.pop(), c) is False:
            return 'NO'
    
    return 'YES' if len(nx) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
