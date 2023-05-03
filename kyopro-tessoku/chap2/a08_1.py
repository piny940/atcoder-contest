h, w = list(map(int, input().split()))
xarr = []
for i in range(h):
  xarr.append(list(map(int, input().split())))

q = int(input())

sums = [[0] * (w + 1)]
for i in range(h):
  row = [0]
  for j in range(w):
    row.append(row[-1] + xarr[i][j])
  sums.append(row)

for i in range(1, w+1):
  for j in range(1, h+1):
    sums[j][i] = sums[j-1][i] + sums[j][i]

for i in range(q):
  a, b, c, d = list(map(int, input().split()))
  print(sums[c][d] - sums[c][b-1] - sums[a-1][d] + sums[a-1][b-1])
