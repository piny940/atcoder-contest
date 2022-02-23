import numpy as np


n, a, b = list(map(np.int64, input().split()))
p, q, r, s = list(map(np.int64, input().split()))


def is_black(x, y):
    value = False
    if x - a == y - b:
        k = x - a
        value = (max(1 - a, 1 - b) <= k <= min(n - a, n - b)) or value
    if x - a == b - y:
        k = x - a
        value = (max(1 - a, b - n) <= k <= min(n - a, b - 1)) or value
    
    return value

ansrr = np.full((q - p + 1, s - r + 1), '')

for i in range(q - p + 1):
    for j in range(s - r + 1):
        if is_black(p+i, r+j):
            ansrr[i, j] = '#'
        else:
            ansrr[i, j] = '.'
    print(''.join(ansrr[i]))
