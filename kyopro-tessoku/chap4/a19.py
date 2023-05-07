import math

n, w = list(map(int, input().split()))
wrr = []
vrr = []

for i in range(n):
  weight, value = list(map(int, input().split()))
  wrr.append(weight)
  vrr.append(value)

values = [[-1 * math.inf] * (w + 1) for i in range(n)]

values[0][0] = 0
if wrr[0] <= w:
  values[0][wrr[0]] = vrr[0]

for i in range(1, n):
  for j in range(w + 1):
    values[i][j] = values[i - 1][j]
    if j >= wrr[i]:
      values[i][j] = max(values[i][j], values[i - 1][j - wrr[i]] + vrr[i])

ans = 0

for v in values[-1]:
  if v == None:
    continue
  ans = max(ans, v)

print(ans)
