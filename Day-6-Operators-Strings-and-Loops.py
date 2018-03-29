import sys

t = int(input())
output = []

for i in range(0, t):
    text = list(sys.stdin.readline().strip())
    output.append([text[0:len(text):2], text[1:len(text):2]])

print("\n")

for k in range(0, len(output)):
    print(''.join(output[k][0]) + ' ' + ''.join(output[k][1]))
