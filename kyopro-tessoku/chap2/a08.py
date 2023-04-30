h, w = list(map(int, input().split()))

xarr = []
for row in range(h):
  xs = list(map(int, input().split()))
  xarr.append(xs)

q = int(input())

sums = []
for row in range(h+1):
  sums.append([0] * (w+1))

for row in range(1, h+1):
  for col in range(1, w+1):
    sums[row][col] = sums[row][col-1] + sums[row-1][col] - sums[row-1][col-1] + xarr[row-1][col-1]

for i in range(q):
  a, b, c, d = list(map(int, input().split()))
  print(sums[c][d] - sums[c][b-1] - sums[a-1][d] + sums[a-1][b-1])
