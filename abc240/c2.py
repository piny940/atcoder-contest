import numpy as np


n, x = list(map(int, input().split()))
ablerr = np.full((n+1, x+1), False)

arr, brr = [0], [0]

for i in range(n):
    a, b = list(map(int, input().split()))
    arr.append(a)
    brr.append(b)

for i in range(1, n+1):
    a, b = arr[i], brr[i]
    for j in range(1, x+1):
        if i == 1:
            ablerr[i, j] = (j == a or j == b)
            continue
        a_ok = (j - a > 0 and ablerr[i-1, j-a])
        b_ok = (j - b > 0 and ablerr[i-1, j-b])
        ablerr[i, j] = a_ok or b_ok

ans = ablerr[n, x]

if ans:
    print('Yes')
else:
    print('No')
