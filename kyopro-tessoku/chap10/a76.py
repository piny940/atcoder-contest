
from bisect import bisect_left


MOD = 1000000007

n, w, l, r = list(map(int, input().split()))
xrr = [0] + list(map(int, input().split())) + [w]

diffs = [0] * (n + 2)
sums = [0] * (n + 2)

sums[0] = 1
diffs[1] = -1
for i in range(n + 1):
  rangel = bisect_left(xrr, xrr[i] + l)
  ranger = bisect_left(xrr, xrr[i] + r + 1)
  if rangel < len(diffs):
    diffs[rangel] += sums[i]
  if ranger < len(diffs):
    diffs[ranger] -= sums[i]
  sums[i + 1] = (sums[i] + diffs[i + 1]) % MOD

print(sums[-1])
