#!/bin/python3

import sys


N = int(input().strip())

if N % 2 != 0:
    print("Weird")  # If N is odd, print Weird

elif N % 2 == 0:

    if 2 <= N <= 5:
        print("Not Weird")  # If N is even and in the inclusive range of 2 to 5, print Not Weird

    elif 6 <= N <= 20:
        print("Weird")  # If N is even and in the inclusive range of 6 to 20, print Weird

    else:
        print("Not Weird")  # If N is even and greater than 20, print Not Weird
