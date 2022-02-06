import numpy as np

n = np.int64(input())
if n == 0:
    print('Yes')

if n > 0:
    if np.log2(n) < 31:
        print('Yes')
    else:
        print('No')

if n < 0:
    if np.log2(-n) <= 31:
        print('Yes')
    else:
        print('No')
        