# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 03:35:52 2019

@author: Sudharshan
"""

from collections import Counter

class SegmentTree():
    def __init__(self, nums):
        self.lower_bound = 0
        self.upper_bound = len(nums) - 1
        self.t = self.__build(nums, 1, 0, len(nums) - 1)
        
    def __build(self, nums, idx, tl, tr):
        t = [0] * len(nums) * 4
        counter = Counter()
        def builder(idx, tl, tr):
            if tl == tr:
                counter[0] += 1
                t[idx] = nums[tl]
            elif tl < tr:
                counter[0] += 1
                tm = int((tl + tr) / 2)
                builder(idx << 1, tl, tm)
                builder((idx << 1) + 1, tm + 1, tr)
                t[idx] = t[idx << 1] + t[(idx << 1) + 1]
        builder(1, tl, tr)
        return t[:counter[0] + 1]
    
    def sum_query(self, l, r):
        if l < self.lower_bound or r > self.upper_bound:
            raise IndexError("The query indices are invalid!")
            
        def sm(idx, tl, tr):
            if tl > tr:
                return 0
            elif tl == l and tr == r:
                return self.t[idx]
            tm = int((tl + tr) / 2)
            if r <= tm:
                return sm(2 * idx, tl, tm)
            elif l > tm:
                return sm(2 * idx + 1, tm + 1, tr)
            else:
                return sm(2 * idx, l, tm) + sm(2 * idx + 1, tm + 1, r)
            
        return sm(1, 0, self.upper_bound)
    
    def update(self, pos, val):
        if pos < self.lower_bound or pos > self.upper_bound:
            raise IndexError("Index out of range!")
            
        def upd(idx, tl, tr):
            if tl == tr:
                self.t[idx] = val
            else:
                tm = int((tl + tr) / 2)
                if pos > tm:
                    upd(2 * idx + 1, tm + 1, tr)
                else:
                    upd(2 * idx, tl, tm)
                    
                self.t[idx] = self.t[2 * idx] + self.t[2 * idx + 1]
        
        upd(1, self.lower_bound, self.upper_bound)
    
    def __unicode__(self):
        return str(self.t)
    
    def __repr__(self):
        return str(self.t)
    
    def __str__(self):
        return str(self.t)