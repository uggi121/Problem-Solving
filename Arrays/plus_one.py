# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:19:56 2019

@author: Sudharshan
"""

def plus_one(digits):
    
    carry = 0
    for i in reversed(range(len(digits))):
        if carry == 0 and i != len(digits) - 1:
            break
        value = digits[i] + 1
        if value > 9:
            carry = 1
        else:
            carry = 0
        digits[i] = value % 10
        
    if carry == 1:
        digits.insert(0, 1)
    return digits