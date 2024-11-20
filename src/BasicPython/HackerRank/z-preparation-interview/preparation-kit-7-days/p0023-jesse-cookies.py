#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def shift_right(heap, idx):
    hlen = len(heap)
    
    while True:
        curr, left, right = idx, idx * 2 + 1, idx * 2 + 2
        
        if left < hlen and heap[curr] > heap[left]:
            curr = left
        if right < hlen and heap[curr] > heap[right]:
            curr = right
            
        if curr != idx:
            heap[curr], heap[idx] = heap[idx], heap[curr]
            idx = curr
        else:
            break
        
def shift_left(heap, idx):
    item = heap[idx]
    
    while idx > 0:
        left = (idx - 1) >> 1
        if heap[left] > item:
            heap[idx] = heap[left]
            idx = left
        else:
            heap[idx] = item
            break
        
def pop(heap):
    hn = len(heap)
    
    if hn == 1:
        return heap.pop()
        
    item = heap[0]
    heap[0] = heap.pop()
    shift_right(heap, 0)
    
    return item

def push(heap, item):
    heap.append(item)
    shift_left(heap, len(heap)-1)

def cookies(k, A):
    # Write your code here
    heap = [i for i in A]
    
    for i in range((n >> 1) - 1, -1, -1):
        shift_right(heap, i)
        
    d = 0
    
    while len(heap) > 1:
        m1 = pop(heap)
        
        if m1 >= k:
            return d
        
        m2 = pop(heap)
        
        x = m1 + m2 * 2
        push(heap, x)
        d += 1
        
    return -1 if heap[0] < k else d
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
