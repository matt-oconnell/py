#!/usr/bin/env python

"""Matt O'Connell -- HW 1.2: Fibonacci Series"""

import sys

user_number = sys.argv[1]

last2 = [1,1]

print last2[0],last2[1],

while last2[1] < float(user_number):
    print last2[1],
    last2 = [last2[1], last2[0] + last2[1]]
