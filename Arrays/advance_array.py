# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 02:30:01 2019

@author: Sudharshan
"""

def advance_array(nums):
    
    can = [0] * len(nums) 
    can[-1] = 1
    
    def dp(i):
        if not can[i]:
            can[i] = -1
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                if dp(j) == 1:
                    can[i] = 1
                    break
        return can[i]

    return True if dp(0) == 1 else False