# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:16:47 2021

@author: Hadar
"""
def revword(word:str) -> str:
    new=""
    for letter in word:
        nl=letter.lower()
        new=nl+new
    return new

def countword() -> int:
    text= open('text.txt')
    word=""
    for line in text:
        word=line.split()[0]
        word=revword(revword(word))
        break
    count=0
    for line in text:
        words=line.split()
        for wrd in words:
            if revword(wrd)==word:
                count+=1
    return(count+1)

