import math

n, w = list(map(int, input().split()))
wrr = []
vrr = []

MAX_VALUE = 1000

for i in range(n):
  weight, value = list(map(int, input().split()))
  wrr.append(weight)
  vrr.append(value)

weights = [[math.inf] * (n * MAX_VALUE + 1) for i in range(n)]

weights[0][0] = 0
weights[0][vrr[0]] = wrr[0]

for i in range(1, n):
  for j in range(n * MAX_VALUE + 1):
    if j >= vrr[i]:
      weights[i][j] = min(weights[i - 1][j], weights[i - 1][j - vrr[i]] + wrr[i])
    else:
      weights[i][j] = weights[i - 1][j]

for i in reversed(range(n * MAX_VALUE + 1)):
  if weights[-1][i] <= w:
    print(i)
    break
