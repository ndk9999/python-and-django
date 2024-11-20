#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPalindrome(s):
    i = 0
    j = len(s) - 1
    
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
        
    return i >= j

def palindromeIndex(s):
    n = len(s)
    i = 0
    j = n - 1
    
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
        
    if i >= j:
        return -1
        
    if isPalindrome(s[i+1:j+1]):
        return i
        
    if isPalindrome(s[i:j]):
        return j
        
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
