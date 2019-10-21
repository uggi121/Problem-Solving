# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:20:57 2019

@author: Sudharshan
"""

def string_to_int(x):
    sign = -1 if x[0] == '-' else 1
    res, power = 0, 0

    for i in reversed(range(1, len(x))):
        res += (ord(x[i]) - 48) * 10**power
        power += 1
    
    if sign == 1:
        res += (ord(x[0]) - 48) * 10**power
    return sign * res