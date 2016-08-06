#!/usr/bin/python
#Problem        : Yet Another Compliance Problem
#Language       : Python
#by Joe Velardo

from __future__ import print_function
from itertools import permutations
import sys

def is_palindrome(word):
    length = len(word)
    if length%2 == 0:
       split_len = length/2
       half1 = word[0:split_len]
       half2 = word[split_len:length]
    else:
       center = length/2
       half1 = word[0:center+1]
       half2 = word[center:length]
        
    half2 = half2[::-1]    

    if half1 == half2:
       return(1)
    else:
       return(0)

entry = raw_input()

chk_list = list(set(permutations(entry,len(entry))))

count = 0

for x in chk_list:
    if is_palindrome(x) > 0:
       count += 1

print(count)
