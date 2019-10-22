# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:30:10 2019

@author: Sudharshan
"""

from linked_list import *

def merge_sorted_lists(L1, L2):
   
    dummy_head = tail = ListNode(0)
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    tail.next = L1 or L2
    
    return dummy_head.next
        
def main():
    l1, l2 = LinkedList(), LinkedList()
    l1.add(5)
    l1.add(6)
    l1.add(8)
    l2.add(3)
    l2.add(4)
    l2.add(7)
    l2.add(9)
    L = merge_sorted_lists(l1.get_head(), l2.get_head())
    ptr = L
    while ptr:
        print(ptr.data, end=' ')
        ptr = ptr.next
        
if __name__ == "__main__":
    main()
    