#!/usr/bin/env python

"""Matt O'Connell -- HW 1.3: Find Primes"""

user_int = int(raw_input('Please enter max integer: '))

def isPrime(int):
    isPrime = True
    for i in range(2, int):
        if int % i == 0:
            isPrime = False
            break
    return isPrime

print 2
for i in range(3, user_int):
    if(isPrime(i)):
        print(i)
