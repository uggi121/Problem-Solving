# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:12:26 2019

@author: Sudharshan
"""

def overlapping_linked_lists(L1, L2):
    len1, len2, ptr1, ptr2 = 0, 0, L1, L2
    
    while ptr1:
        len1 += 1
        ptr1 = ptr1.next
        
    while ptr2:
        len2 += 1
        ptr2 = ptr2.next
    
    diff = int(abs(len2 - len1))
    
    ptr1, ptr2 = L1, L2
    if len1 < len2:
        for i in range(diff):
            ptr2 = ptr2.next
    else:
        for i in range(diff):
            ptr1 = ptr1.next
            
    while ptr1 and ptr2:
        if ptr1 is ptr2:
            return True
        ptr1, ptr2 = ptr1.next, ptr2.next
    
    return False