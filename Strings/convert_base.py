# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:18:35 2019

@author: Sudharshan
"""

def convert_base(inp, b1, b2):
    def convert_to_decimal(x, b):
        res = 0
        for i in reversed(range(len(x))):
            res += int(x[i]) * b ** (len(x) - 1 - i)
        return res
    
    def convert(x):
        return x if x < 10 else chr(ord('A') + (x % 10))
    
    dec = convert_to_decimal(inp, b1)
    result = []
    
    while dec != 0:
        result.append(str(convert(dec % b2)))
        dec //= b2
    
    result.reverse()
    return ''.join(result)