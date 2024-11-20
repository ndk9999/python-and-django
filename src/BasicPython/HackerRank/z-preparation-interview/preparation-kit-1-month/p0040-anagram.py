#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    
    if n & 1 == 1:
        return -1
    
    i = 0
    j = n - 1
    a = [0] * 26
    b = [0] * 26
    
    while i < j:
        a[ord(s[i]) - 97] += 1
        b[ord(s[j]) - 97] += 1
        i += 1
        j -= 1
        
    count = 0
    for i in range(26):
        count += abs(a[i] - b[i])
            
    return count // 2
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
