#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    counter = [0] * 26
    
    for c in s.lower():
        if c.isalpha():
            counter[ord(c) - 97] += 1
        
    return 'not pangram' if counter.count(0) > 0 else 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
