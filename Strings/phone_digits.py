# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:44:01 2019

@author: Sudharshan
"""

import functools

mapping = {
           '2' : ['A', 'B', 'C'],
           '3' : ['D', 'E', 'F'],
           '4' : ['G', 'H', 'I'],
           '5' : ['J', 'K', 'L'],
           '6' : ['M', 'N', 'O'],
           '7' : ['P', 'Q', 'R', 'S'],
           '8' : ['T', 'U', 'V'],
           '9' : ['W', 'X', 'Y', 'Z']
           }

def phone_digits(inp):
    if not inp:
        return []
    if len(inp) == 1:
        return mapping[inp]
    
    so_far = phone_digits(inp[1:])
    current = mapping[inp[0]]
    return functools.reduce(lambda so_far, new_list : so_far + new_list,
            list(map(lambda x: list(map(lambda y: x + y, so_far)), current)))
