# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:37:42 2019

@author: Sudharshan
"""

from collections import Counter

def build_segment_tree(arr):
    segment_tree = [0] * (4 * len(arr))
    count = Counter()
    
    def build(idx, l, r):
        if l == r:
            count['elements'] += 1
            segment_tree[idx] = arr[l]
        elif l < r:
            count['elements'] += 1
            segment_tree[idx] = (build(2 * idx, l, int((r + l) / 2))
                    + build(2 * idx + 1, int((r + l) / 2) + 1, r))
        return segment_tree[idx]
    
    build(1, 0, len(arr) - 1)
    return segment_tree[:count['elements'] + 1]
            
def sum_query(idx, t, tl, tr, l, r):
    if l > r:
        return 0
    elif tl == l and tr == r:
        return t[idx]
    else:
        tm = int((tl + tr) / 2)
        return (sum_query(2 * idx, t, tl, tm, l, min(r, tm))
            + sum_query(2 * idx + 1, t, tm + 1, tr, max(l, tm + 1), r))
        
def query(arr, t, l, r):
    return sum_query(1, t, 0, len(arr) - 1, l, r)

def update(idx, pos, val, tl, tr, t):
    if tl == tr:
        t[idx] = val
    else:
        tm = int((tl + tr) / 2)
        if pos > tm:
            update(2 * idx + 1, pos, val, tm + 1, tr, t)
        else:
            update(2 * idx, pos, val, tl, tm, t)
        t[idx] = t[2 * idx] + t[2 * idx + 1]
        
        
        