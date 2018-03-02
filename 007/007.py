#!python3
# -*- coding: utf-8 -*-

"""
10001st prime
-------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
Utilizo la criba de Eratóstenes
"""
MAX = 500000 # Máximo número a tratar (arbitrario)

M = 10001

numeros = [None] * MAX
# numeros[true] -> número marcado (no primo)
# numeros[None] -> número sin marcar (o primo no tratado)

nPrimos = 0 # Número de primos calculados

for i in range(2, MAX):
    if numeros[i] == None:
        nPrimos += 1
        if nPrimos == M:
            print i
            break
        for j in range(i, MAX/i):
            numeros[i*j] = True

