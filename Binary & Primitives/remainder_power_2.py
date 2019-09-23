# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 03:11:23 2019

@author: Sudharshan
"""

def remainder_power_2(x, power):
    y = 1 << (power - 1)
    y = y | (y - 1)
    return x & y

