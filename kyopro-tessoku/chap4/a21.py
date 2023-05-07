n = int(input())
prr = []
arr = []

for i in range(n):
  p, a = list(map(int, input().split()))
  prr.append(p - 1)
  arr.append(a)

dps = [[None] * n for i in range(n)]
# 0行目
for r in reversed(range(n)):
  if r == n - 1:
    dps[0][r] = 0
    continue
  score = arr[r + 1] if prr[r + 1] <= r else 0
  dps[0][r] = dps[0][r + 1] + score

for l in range(1, n):
  for r in reversed(range(l, n)):
    score_l = arr[l - 1] if prr[l - 1] >= l and prr[l - 1] <= r else 0

    if r == n - 1:
      dps[l][r] = dps[l - 1][r] + score_l
      continue

    score_r = arr[r + 1] if prr[r + 1] >= l and prr[r + 1] <= r else 0
    dps[l][r] = max(dps[l - 1][r] + score_l, dps[l][r + 1] + score_r)

ans = 0
for i in range(n):
  ans = max(ans, dps[i][i])

print(ans)
