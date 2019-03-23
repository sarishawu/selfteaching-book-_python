#!/usr/bin/env python3

"""
A Python version of the classic "bottles of beer on the wall" programming
example.

By Guido van Rossum, demystified after a version by Fredrik Lundh.
"""
# sys.argv   
import sys

n = 100

if sys.argv[1:]:
    n = int(sys.argv[1]) 
#这个是一个类似备选项。如果你不传参数，n就是100，如果传参数，传就就是几的。在terminal可以这样python beer.py 10

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")
