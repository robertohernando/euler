#!python3
# -*- coding: utf-8 -*-

"""
Summation of primes
-------------

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
Voy calculando todos los primos con la criba de Eratóstones
y calculando el sumatorio
"""

MAX = 2000000
suma = 0

numeros = [None] * MAX
# numeros[true] -> número marcado (no primo)
# numeros[None] -> número sin marcar (primo o no tratado)

for i in range(2, MAX):
    if numeros[i] == None:
        for j in range(i, MAX/i+1):
            if i*j < MAX:
                numeros[i*j] = True

# Sumo todos los números sin marcar, que serán los primos
for i in range(2, MAX):
    if numeros[i] == None:
        suma += i

print suma

