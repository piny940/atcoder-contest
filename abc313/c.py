import math

n = int(input())
arr = list(map(int, input().split()))
count = 0
arr.sort()
minv = arr[0]
diffs1 = []
for i in range(1, n):
  diffs1.append(arr[i] - arr[i - 1])
diffs2 = [-v for v in diffs1]

idx1 = 0
idx2 = n - 1

while idx1 < idx2:
  abs1 = abs(diffs1[idx1])
  abs2 = abs(diffs2[idx2])
  if abs1 > abs2:
    diffs1[idx1] -= abs2
    idx2 -= 1
    count += abs2
  elif abs1 < abs2:
    diffs2[idx2] -= abs1
    idx1 += 1
    count += abs1
  elif abs1 == abs2:
    abs1 += 1
    abs2 -= 1
    count += abs1

count += (diffs1[idx1] - diffs2[idx2])
