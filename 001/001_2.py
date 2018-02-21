#!python3

# Second version
# Optimized
MAX = 999

def sumDiv(n):
    p = MAX/n
    return n*(p*(p+1))/2

print (sumDiv(3) + sumDiv(5) - sumDiv(15))
