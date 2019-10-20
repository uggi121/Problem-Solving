# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:38:30 2019

@author: Sudharshan
"""

def buy_sell_stock(prices):
    max_profit = 0
    buy = prices[0]
    
    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit = prices[i] - buy
            max_profit = max(profit, max_profit)
        else:
            buy = prices[i]
            
    return max_profit