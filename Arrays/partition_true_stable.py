# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:00:29 2019

@author: Sudharshan
"""

def partition_stable(bools, key=lambda x: x):
    
    t, f = len(bools), len(bools) - 1
    while f >= 0:
        if key(bools[f]):
            t -= 1
            bools[f], bools[t] = bools[t], bools[f]
        f -= 1
    return bools
        
    