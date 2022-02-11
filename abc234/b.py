import numpy as np


n = int(input())

coords = []

for i in range(n):
    coords.append(tuple(map(int, input().split())))

def d(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

maxdis = 0

for i in range(n):
    a = coords[i]
    for j in range(n):
        if i == j:
            continue
        b = coords[j]
        maxdis = max(maxdis, d(a, b))

print(maxdis)
