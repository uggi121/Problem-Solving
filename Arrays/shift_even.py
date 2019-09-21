# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:19:56 2019

@author: Sudharshan
"""

def shift_even(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        while r >= 0 and nums[r] % 2 == 1:
            r -= 1
        if l >= r:
            break
        while l < len(nums) and nums[l] % 2 == 0:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    return nums

def shift_even_two(nums):
    l, r = -1, 0
    while r < len(nums):
        if nums[r] % 2 == 0:
            l += 1
            nums[l], nums[r] = nums[r], nums[l]
        r += 1
    return nums