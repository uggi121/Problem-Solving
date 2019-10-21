# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:09:09 2019

@author: Sudharshan
"""

from collections import deque

def int_to_string(x):
    if x < 0:
        return '-' + int_to_string(-x)
    q = deque()
    
    while x != 0:
        q.appendleft(chr(x % 10 + 48))
        x //= 10
    
    if q:
        return ''.join(q)
    return '0'
        
    