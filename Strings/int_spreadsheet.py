# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:55:50 2019

@author: Sudharshan
"""

from collections import deque

def integer_to_column(x):
    res = deque()
    
    while x != 0:
        res.appendleft(chr((x - 1) % 26 + ord('A')))
        x = (x - 1) // 26
    
    return ''.join(res)