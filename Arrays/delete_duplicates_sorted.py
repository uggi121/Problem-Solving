# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:04:34 2019

@author: Sudharshan
"""

def del_dups_partition(nums):
    for idx, val in enumerate(nums):
        if val == nums[idx - 1]:
            nums[idx - 1] = 'x'
    
    sort = -1
    
    for deleted in range(len(nums)):
        if nums[deleted] != 'x':
            sort += 1
            nums[sort], nums[deleted] = nums[deleted], nums[sort]
    
    return nums

def del_dups_window(nums):
    start = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[start + 1] = nums[i]
            start += 1
        
    return nums
    
            
    