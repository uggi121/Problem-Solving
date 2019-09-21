# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:46:59 2019

@author: Sudharshan
"""

def add_binary(bs, bt):
    if len(bs) < len(bt):
        return add_binary(bt, bs)
    
    pad_length = len(bs) - len(bt)
    
    b_s = [int(char) for char in bs]
    b_t = [0] * pad_length
    b_t.extend(int(char) for char in bt)
    
    result = []
    
    carry = 0
    for i in reversed(range(len(bs))):
        value = b_s[i] + b_t[i]
       
        result.append((value + carry) % 2)
        if value >= 2:
            carry = 1
        else:
            carry = 0
    if carry == 1:
        result.append(1)
    
    return list(reversed(result))
    