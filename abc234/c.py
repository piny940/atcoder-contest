import numpy as np


k0 = np.int64(input()) + 1

i = np.int64(np.floor(np.log2(k0) + 1))

ansarr = []

def explore(digits_num, k1):
    if digits_num == 0:
        return
    
    if k1 > 2 ** (digits_num - 1):
        k1 -= 2 ** (digits_num - 1)
        ansarr.append('2')
    else:
        ansarr.append('0')
    explore(digits_num - 1, k1)

explore(i, k0)

for i in range(len(ansarr)):
    if ansarr[0] == '0':
        ansarr.remove('0')
    else:
        break

print(''.join(ansarr))
