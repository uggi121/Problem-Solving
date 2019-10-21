# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:26:52 2019

@author: Sudharshan
"""

def reverse_words_in_sentence(sentence):
    sentence.reverse()
    fwd, bck = 0, 0
    
    while fwd < len(sentence):
        while fwd < len(sentence) and sentence[fwd].isalpha():
            fwd += 1
        for i in range(bck, (bck + fwd)//2):
            sentence[i], sentence[fwd - (i - bck) - 1] = sentence[fwd - (i - bck) - 1], sentence[i]
            
        fwd += 1
        bck = fwd
    
    return sentence

sent = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e']

reverse_words_in_sentence(sent)