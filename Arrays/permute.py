# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:26:40 2019

@author: Sudharshan
"""

def permute(perm, A):
    
    for i in range(len(A)):
        j = perm[i]
        A[i], A[j] = A[j], A[i]
        perm[i], perm[j] = perm[j], perm[i]
    
    return A

def perm_arr(perm, A):
    res = [0] * len(A)
    for i in range(len(A)):
        res[i] = A[perm[i]]
    
    return res