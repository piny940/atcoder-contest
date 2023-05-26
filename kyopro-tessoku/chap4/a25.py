h, w = list(map(int, input().split()))

cmat = []
for _ in range(h):
  row = list(input())
  cmat.append(row)

ways = [[0] * w for _ in range(h)]
ways[0][0] = 1
for j in range(1, w):
  if cmat[0][j] == '.':
    ways[0][j] = ways[0][j - 1]

for i in range(1, h):
  for j in range(0, w):
    if cmat[i][j] == '#':
      continue
    if j == 0:
      ways[i][j] = ways[i - 1][j]
      continue
    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

print(ways[h - 1][w - 1])
