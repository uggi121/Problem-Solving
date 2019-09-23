# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 03:18:09 2019

@author: Sudharshan
"""

def power_of_2(x):
    return x == (x & ~(x - 1))