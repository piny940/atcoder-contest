import numpy as np


s = 'a' * 10**6

while True:
    if s[-1] != 'a':
        break
    else:
        s = s[:-1]

l = len(s)

if s == s[::-1]:
    print('Yes')
else:
    print('No')

