#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, info):
        self.info = info
        self.children = []
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = Node('')

    def create(self, word):
        current = self.root
        
        for c in word:
            child = None
            
            for node in current.children:
                if node.info == c:
                    child = node
                    break
            if child is None:
                child = Node(c)
                current.children.append(child)
                current = child
            elif len(child.children) == 0:
                return word
            else:
                current = child
                
        if len(current.children) > 0:
            return word
        else:
            return ''
#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    tree = BinarySearchTree()
    r = ''
    
    for w in words:
        r = tree.create(w)
        if r != '':
            break
        
    if r == '':
        print('GOOD SET')
    else:
        print('BAD SET')
        print(r)

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
