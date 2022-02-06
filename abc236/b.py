import numpy as np


n = int(input())
arr = list(map(int, input().split()))

sum = 4 * n * (n + 1) // 2
print(sum - np.sum(arr))
