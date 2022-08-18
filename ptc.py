import math
import os
import random
import re
import sys
# Complete the 'alternate' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def char_range(i, j):
    for a in range(ord(i), ord(j)+1):
        yield chr(a)
def is_alternating(s):
    for i in range(len(s) - 1):
        if(s[i] == s[i+1]):
            return False
    return True
def alternate(s):
    # Write your code here
    ml = 0
    for i in char_range('a', 'z'):
        for j in char_range('a', 'z'):
            if(i == j):
                continue
            n_st = [ch for ch in s if ch==i or ch ==j]
            n_st_l = len(n_st)
            if(is_alternating(n_st) and n_st_l > 1):
                if(n_st_l > ml):
                    ml = n_st_l
    return ml
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()
    result = alternate(s)
    fptr.write(str(result) + '\n')
    fptr.close()