import numpy as np


N = int(input())
As = list(map(int, input().split()))

cuts = []
current = 0

for i in range(N):
    a = As[i]
    current += a
    cuts.append(current % 360)

cuts.sort()

diffs = []
diffs.append(cuts[0])
for i in range(N - 1):
    diffs.append(cuts[i + 1] - cuts[i])
diffs.append(360 - cuts[N - 1])

print(np.amax(diffs))
