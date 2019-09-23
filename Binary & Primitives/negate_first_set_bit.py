# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 03:01:56 2019

@author: Sudharshan
"""

def negate_first_set_bit(x):
    return x & (x - 1)