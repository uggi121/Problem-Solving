# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 02:59:53 2019

@author: Sudharshan
"""

def isolate_first_set_bit(x):
    return x & ~(x - 1)