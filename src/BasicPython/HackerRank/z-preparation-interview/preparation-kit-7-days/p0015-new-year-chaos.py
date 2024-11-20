#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def merge(q, li, m, ri):
    if li >= ri:
        return 0
    
    d = 0
    ln = m - li + 1
    rn = ri - m
    la = q[li:m+1]
    ra = q[m+1:ri+1]
    i = 0
    j = 0
    
    #print(la, ln, ra, rn)
    
    while i < ln and j < rn:
        if la[i] <= ra[j]:
            q[li + i + j] = la[i]
            i += 1
        else:
            q[li + i + j] = ra[j]
            d += ln - i
            j += 1
    
    while i < ln:
        q[li + i + j] = la[i]
        i += 1
        
    while j < rn:
        q[li + i + j] = ra[j]
        j += 1
    
    return d

def count_pair(q, li, ri):
    c = 0
    if li < ri:
        m = (li + ri) // 2
        c += count_pair(q, li, m)
        c += count_pair(q, m+1, ri)
        c += merge(q, li, m, ri)
    return c

def minimumBribes(q):
    s = 0
    
    for i in range(n):
        d = q[i] - i - 1
        if d > 2:
            s = -1
            break
        
    if s < 0:
        print('Too chaotic')
    else:
        s = count_pair(q, 0, n-1)
        print(s)
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
