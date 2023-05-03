n = int(input())

h = 1500
w = 1500

points = [[0] * w for i in range(h)]

for i in range(n):
  x, y = list(map(int, input().split()))
  points[y-1][x-1] += 1

q = int(input())

sums = [[0] * (w+1) for i in range(h+1)]

for i in range(h):
  for j in range(w):
    sums[i+1][j+1] = sums[i+1][j] + points[i][j]

for i in range(w):
  for j in range(h):
    sums[j+1][i+1] = sums[j][i+1] + sums[j+1][i+1]

for i in range(q):
  a, b, c, d = list(map(int, input().split()))
  print(sums[d][c] - sums[d][a-1] - sums[b-1][c] + sums[b-1][a-1])
