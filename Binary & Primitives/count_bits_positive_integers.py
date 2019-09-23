# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 02:32:22 2019

@author: Sudharshan
"""

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits