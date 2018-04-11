#!/bin/python3

import sys

# function to take size input and validate
def enterLength():
    number = int(input().strip())
    if 1 <= number <= 100000:
        return number
    else:
        print("You entry does not satisfy constraint 1 <= N <= 100,000")
        enterLength()


# function to get inputs
def getInputs(arr):
    entry = str(input())

    for y in range(0, 100000):
        if not entry:
            return arr
        else:
            arr.append(entry)


phoneBook = {}
outputTexts = []
query = []
inputs = []
vals = int(enterLength())

# Take dictionary entry
for x in range(0, vals):
    text = input().split()
    phoneBook[text[0]] = text[1]

# Take query
inputs = getInputs(query)

for y in range(0, len(inputs)):
    if inputs[y] in phoneBook:
        outputTexts.append(str(query) + '=' + str(phoneBook[query]))
    else:
        outputTexts.append('Not found')


for output in range(0, len(outputTexts)):
    print(outputTexts[output])
