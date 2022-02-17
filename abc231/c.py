import numpy as np


n, q = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr = list(reversed(np.sort(arr)))

xrr = []
for i in range(q):
    xrr.append(int(input()))
args_sorted = list(reversed(np.argsort(xrr)))

tmp = 0
ansrr = np.zeros(q, dtype=int)

idx = 0
arg = args_sorted[idx]
finished = False

for i in range(n):
    while arr[i] < xrr[arg]:
        ansrr[arg] = tmp
        idx += 1
        if idx >= q:
            finished = True
            break
        arg = args_sorted[idx]
    if finished:
        break
    tmp += 1
    ansrr[arg] = tmp

for i in range(idx+1, q):
    ansrr[args_sorted[i]] = tmp

for i in range(len(ansrr)):
    print(ansrr[i])
