#!python3
# -*- coding: utf-8 -*-

"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def esPalindromo(n):
    a = []
    for e in str(n):
        a.append(int(e))
    
    for i in range(0,len(a)/2):
        if a[i]!=a[len(a)-i-1]:
            return None
    return True

maxPal=0

for i in range(999, 100, -1):
    for j in range(999, i, -1):
        if esPalindromo(i*j):
            maxPal = max(maxPal, i*j)

print maxPal
