# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:55:42 2019

@author: Sudharshan
"""

def alternation(nums):
    high = True
    
    for i in range(1, len(nums)):
        if high:
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        else:
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        high = not high
    
    return nums