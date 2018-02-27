#!python3
# -*- coding: utf-8 -*-

"""
Smallest multiple
-----------------

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

N = 20

# Mínimo común múltiplo
def mcm(a,b):
    return(a*b / mcd (a,b))

# Máximo común divisor
def mcd(a,b):
    if a < b:
        return mcd(b,a)
    else:
        c = a/b
        r = a%b
        if r == 0:
            return b
        else:
            return mcd(b,r)

# Resolución del problema
n = 1
for i in range (2, N):
    n = mcm (i, n)

print n
