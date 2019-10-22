# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:18:23 2019

@author: Sudharshan
"""

def remove_over_k(L, k):
    
    dummy_node = prev = ListNode(0, L)
    
    ptr = L
    
    while ptr:
        count = 1
        while ptr.next and ptr.next.data == prev.next.data:
            ptr = ptr.next
            count += 1
        
        if count > k:
            for i in range(count):
                prev.next = prev.next.next
            ptr = prev.next
        else:
            prev = ptr
            ptr = ptr.next
    
    return dummy_node.next