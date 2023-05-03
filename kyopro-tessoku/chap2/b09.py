n = int(input())
h, w = 1500, 1500

diffs = [[0] * (w + 1) for i in range(h + 1)]

for i in range(n):
  a, b, c, d = list(map(int, input().split()))
  diffs[a][b] += 1
  diffs[c][d] += 1
  diffs[a][d] -= 1
  diffs[c][b] -= 1

sums = [[0] * w for i in range(h)]

for i in range(h):
  prev = 0
  for j in range(w):
    sums[i][j] = prev + diffs[i][j]
    prev = sums[i][j]

for j in range(w):
  prev = 0
  for i in range(h):
    sums[i][j] = prev + sums[i][j]
    prev = sums[i][j]

ans = 0

for i in range(h):
  for j in range(w):
    if sums[i][j] > 0: ans += 1

print(ans)
