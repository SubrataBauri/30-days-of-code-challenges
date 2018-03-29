#!/bin/python3

import sys


n = int(input().strip())
i = 1  # constant to start with

while 1 <= i <= 10:
    print (str(n) + ' x ' + str(i) + " = " + str(n*i))
    i = i + 1
