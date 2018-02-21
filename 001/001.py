#!python3
MAX = 1000

sum = 0

for i in range(3, MAX):
    if (i%3 == 0) or (i%5 == 0):
        sum +=i
print (sum)
