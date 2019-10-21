# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:38:56 2019

@author: Sudharshan
"""

def replace_and_remove(arr, num):
    count_a, write_index = 0, 0
    
    for i in range(num):
        if arr[i] != 'b':
            arr[write_index] = arr[i]
            write_index += 1
        if arr[i] == 'a':
            count_a += 1
    
    write = len(arr) - 1
    
    for i in reversed(range(write_index)):
        if arr[i] == 'a':
            arr[write], arr[write - 1] = 'd', 'd'
            write -= 2
        else:
            arr[write] = arr[i]
            write -= 1
    
    return arr
    
    