# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 02:54:14 2019

@author: Sudharshan
"""

def parity(x):
    shifts = [2 ** i for i in range(5, -1, -1)]
    for i in shifts:
        x ^= x >> i
    return x & 1