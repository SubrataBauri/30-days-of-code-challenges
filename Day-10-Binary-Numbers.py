#!/bin/python3

import sys


n = int(input().strip())

rem = 0
max_rem = 0
binary = []

while n > 0:
    if n % 2 == 1:
        rem = rem + 1
        binary.insert(0, 1)  # insert binary values in reverse order
        if rem > max_rem:
            max_rem = rem
    else:
        rem = 0
        binary.insert(0, 0)  # insert binary values in reverse order

    n = n // 2


print(max_rem)

binary_number = ''
for num in binary:
    binary_number = binary_number + str(num)

print(binary_number)
