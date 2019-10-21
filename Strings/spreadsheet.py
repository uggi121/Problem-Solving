# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:36:37 2019

@author: Sudharshan
"""

def spreadsheet_encoding(x):
    def conv(y):
        return ord(y) - ord('A') + 1
    
    power, res = 0, 0
    for i in reversed(range(len(x))):
        res += conv(x[i]) * 26 ** power
        power += 1
    
    return res