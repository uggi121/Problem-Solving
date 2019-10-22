# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:13:19 2019

@author: Sudharshan
"""

from linked_list import *

def reverse_linked_list(L):
    if not L:
        return L
    
    prev, cur, nxt = ListNode(0, L), L, L.next
    
    while cur:
        cur.next = prev
        prev, cur = cur, nxt
        if nxt:
            nxt = nxt.next
    
    L.next = None
    L = prev
    return prev
    
    
        
        