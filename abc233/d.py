import numpy as np


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        if np.sum(arr[i:j+1]) == k:
            ans += 1

print(ans)
