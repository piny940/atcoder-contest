MAX_POWER = 100
MAX_MOTIV = 100

n, k = list(map(int, input().split()))
counts = [[0] * (MAX_MOTIV + 1) for _ in range(MAX_POWER + 1)]
for i in range(n):
  a, b = list(map(int, input().split()))
  counts[a][b] += 1

sums = [[0] * (MAX_MOTIV + 1) for _ in range((MAX_POWER + 1))]

for i in range(1, MAX_POWER + 1):
  for j in range(MAX_MOTIV + 1):
    sums[i][j] = sums[i - 1][j] + counts[i][j]

for j in range(1, MAX_MOTIV + 1):
  for i in range(MAX_POWER + 1):
    sums[i][j] += sums[i][j - 1]

ans = 0
for i in range(1, MAX_POWER - k + 1):
  for j in range(1, MAX_MOTIV - k + 1):
    tmp = sums[i + k][j + k] - sums[i + k][j - 1] - sums[i - 1][j + k] + sums[i - 1][j - 1]
    ans = max(ans, tmp)

print(ans)
