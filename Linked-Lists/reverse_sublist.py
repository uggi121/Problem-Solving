# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:30:28 2019

@author: Sudharshan
"""

from linked_list import *

def reverse_sublist(L, s, f):
    
    if s >= f:
        return L
    
    dummy_node = start = ListNode(0, L)
    
    for i in range(0, s - 1):
        start = start.next
        
    prev, cur = start.next, start.next.next
    
    for i in range(s, f):
        temp = cur.next
        cur.next = prev
        prev, cur = cur, temp
    
    start.next.next = cur
    start.next = prev
    
    return dummy_node.next
        
    
    
    