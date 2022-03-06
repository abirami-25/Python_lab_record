from operator import xor
from re import I


string = input("Enter a string  :")
words = string.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

for x in d.keys():
    print ("%s occurs %d times "%(x,d[x]))