# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:59:08 2019

@author: Sudharshan
"""

def remove_duplicates_sorted(L):
    
    ptr = L
    while ptr:
        if ptr.next and ptr.next.data == ptr.data:
            ptr.next = ptr.next.next
        ptr = ptr.next
    
    return L