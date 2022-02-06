import numpy as np


H, W = map(int, input().split())

A = np.zeros((H, W), dtype=int)

for i in range(H):
    A[i] = np.array(list(map(int, input().split())))

B = A.T

for i in range(W):
    print(*B[i])
