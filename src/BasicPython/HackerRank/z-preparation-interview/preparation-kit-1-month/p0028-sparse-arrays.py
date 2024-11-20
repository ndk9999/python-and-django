#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, info): 
        self.info = info
        self.count = 0
        self.children = []
        self.level = None 

    def __str__(self):
        return str(self.info) 

class SearchTree:
    def __init__(self): 
        self.root = Node('')

    def add(self, word):
        parent = None
        current = self.root
        i = 0
        m = len(word)
        
        while current is not None and i < m:
            parent = current
            node = None
            for child in current.children:
                if child.info == word[i]:
                    node = child
                    break
            current = node
            if current is not None:
                i += 1
                
        while i < m:
            current = Node(word[i])
            parent.children.append(current)
            parent = current
            i += 1
            
        current.count += 1
    
    def search(self, word):
        current = self.root
        i = 0
        m = len(word)
        
        while current is not None and i < m:
            parent = current
            node = None
            for child in current.children:
                if child.info == word[i]:
                    node = child
                    break
            current = node
            i += 1
            
        if current is None:
            return 0
        else:
            return current.count

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    return [strings.count(c) for c in queries]
    
    # Build tree
    #tree = SearchTree()
    
    #for word in strings:
    #    tree.add(word)
        
    #return [tree.search(w) for w in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
