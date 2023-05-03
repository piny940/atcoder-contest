h, w, n = list(map(int, input().split()))

diffs = [[0] * (w + 1) for i in range(h + 1)]

for i in range(n):
  a, b, c, d = list(map(int, input().split()))
  a, b, c, d = a-1, b-1, c-1, d-1
  diffs[a][b] += 1
  diffs[c+1][d+1] += 1
  diffs[a][d+1] -= 1
  diffs[c+1][b] -= 1

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

for i in range(h):
  print(*sums[i])
