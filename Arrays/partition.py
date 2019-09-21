# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:19:56 2019

@author: Sudharshan
"""

def partition(nums, idx):
    pivot = nums[idx]
    l, p, r = -1, -1, 0
    while r < len(nums):
        if nums[r] == pivot:
            p += 1
            nums[p], nums[r] = nums[r], nums[p]
        elif nums[r] < pivot:
            l += 1
            nums[r], nums[l] = nums[l], nums[r]
            p += 1
            nums[p], nums[r] = nums[r], nums[p]
        r += 1
    
    return nums