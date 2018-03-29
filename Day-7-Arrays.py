#!/bin/python3

import sys


# function to take size input and validate
def enterLength():
    number = int(input().strip())
    if 1 <= number <= 1000:
        return number
    else:
        print("You entry does not satisfy constraint 1 <= N <= 1000")
        enterLength()


# function to take array input and validate the numbers in array
def checkArrayValue(number):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')][:number]
    for value in arr:
        if value < 1 or value > 10000 or value == '':
            print("Array value should be 1 <= N <= 10000")
            arr = checkArrayValue(number)

    return arr


print("Enter number: 1<= N <= 1000")
n = enterLength()

print("Enter array values separated by space: 1 <= array[index] <= 10000")
array = checkArrayValue(n)
reverse = array[::-1]

print(' '.join(map(str, reverse)))
