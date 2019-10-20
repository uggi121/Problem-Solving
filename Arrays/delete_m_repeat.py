# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:42:25 2019

@author: Sudharshan
"""

def delete_m_repeat(nums, m):
    if m <= 2:
        return nums
    
    count, write_index = 1, 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[write_index - 1]:
            count += 1
            if count != m:
                nums[write_index] = nums[i]
                write_index += 1
        else:
            nums[write_index] = nums[i]
            count = 1
            write_index += 1
    
    return nums
    