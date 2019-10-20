# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:50:05 2019

@author: Sudharshan
"""

def maximum_equal_subarray(nums):
    if not nums:
        return 0
    
    max_so_far, count = 1, 1
    
    for i in range(1, len(nums)):
        count = count + 1 if nums[i] == nums[i - 1] else 1
        max_so_far = max(max_so_far, count)
        
    return max_so_far