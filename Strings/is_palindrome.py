# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:18:24 2019

@author: Sudharshan
"""

def is_palindrome(string):
    l, r = 0, len(string) - 1
    while True:
        if l >= r:
            return True
        
        while l < r and not string[l].isalnum():
            l += 1
        
        while r > l and not string[r].isalnum():
            r -= 1
        
        if string[l].lower() != string[r].lower():
            return False
        
        l += 1
        r -= 1