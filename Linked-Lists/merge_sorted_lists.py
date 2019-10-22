# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:30:10 2019

@author: Sudharshan
"""

from linked_list import *

def merge_sorted_lists(L1, L2):
    if not L1:
        return L2
    if not L2:
        return L1
    
    if L1.data > L2.data:
        return merge_sorted_lists(L2, L1)
    
    head1, head2 = L1, L2
    
    while head1 and head2:
        if head1.next and head1.next.data > head2.data:
            temp = head2
            head2 = head2.next
            insert_after(head1, temp)
        elif not head1.next and head1.data < head2.data:
            insert_after(head1, head2)
        else:
            head1 = head1.next
    
    return L1
        
    