# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:02:48 2019

@author: Sudharshan
"""

def buy_sell_stock_twice(prices):
    max_total_profit, min_price_so_far = 0, float('inf')
    
    F = [0] * len(prices)
    
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        F[i] = max(0, max_total_profit)
        
    max_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices))):
        max_so_far = max(price, max_so_far)
        profit = max_so_far - price
        left = F[i - 1] if i > 0 else 0
        max_total_profit = max(max_total_profit,
                               left + profit)
        
    return max_total_profit

def buy_sell_stock_twice_space(prices):
    # O(1) space
    l, r = 0, len(prices) - 1
    min_so_far, max_so_far = float('inf'), float('-inf')
    lp, rp = 0, 0
    
    while True:
        if l >= r:
            break
        
        prev = prices[l - 1] if l > 0 else float('-inf')
        profit = 0
        while l <= r:
            min_so_far = min(min_so_far, prices[l])
            if prices[l] < prev and profit > 0:
                break
            
            prev = prices[l]
            profit = max(prices[l] - min_so_far, profit)
            l += 1
        
        lp = max(lp, profit)
        
        profit = 0
        prev = prices[r + 1] if r < len(prices) - 1 else float('inf')
        while r >= l:
            max_so_far = max(max_so_far, prices[r])
            if prices[r] > prev and profit > 0:
                break
            
            prev = prices[r]
            profit = max(max_so_far - prices[r], profit)
            r -= 1
            
        rp = max(rp, profit)
            
            
        
    return lp + rp
            
        