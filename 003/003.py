#!python3
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#n = 13195
n = 600851475143

p = 2
while n>1:
    while n % p == 0:
        n = n / p
    p += 1

print(p-1)

