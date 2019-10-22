# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:26:45 2019

@author: Sudharshan
"""

from linked_list import *

def reverse_list_group_k(L, k):
    length, length_ptr = 0, L
    
    while length_ptr:
        length += 1
        length_ptr = length_ptr.next
    
    print(length)
    dummy_node = start = ListNode(None, L)
    
    for i in range(length // k):
        prev, cur = start.next, start.next.next
        for j in range(k - 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        start.next.next, tmp = cur, start.next
        start.next = prev
        start = tmp
      
    return dummy_node.next
       
    
        
        
    