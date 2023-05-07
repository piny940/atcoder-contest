import math

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
arr = [0] + arr
brr = [0, 0] + brr

crr = []
drr = []
for i in range(n - 1):
  crr.append(arr[i + 1])
  if i < n - 2:
    drr.append(brr[i + 2])

costs = [math.inf] * n
costs[0] = 0

for i in range(n - 1):
  costs[i + 1] = min(costs[i + 1], costs[i] + crr[i])
  if i < n - 2:
    costs[i + 2] = min(costs[i + 2], costs[i] + drr[i])

print(costs[-1])
