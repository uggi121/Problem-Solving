# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:05:51 2019

@author: Sudharshan
"""

import math

def list_of_primes(n):
    
    def is_prime(n):
        return not any(n % x == 0 for x in range(2, int(math.sqrt(n)) + 1))
    
    return list(filter(is_prime, range(2, n + 1)))

def sieve(n):
    result = []
    
    def is_prime(n):
        return not any(n % x == 0 for x in range(2, int(math.sqrt(n)) + 1))
    
    stream = range(2, n + 1)
    for i in stream:
        if is_prime(i):
            result.append(i)
        stream = filter(lambda x: x % i != 0, stream)
    
    return result