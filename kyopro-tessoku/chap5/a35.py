n = int(input())
arr = list(map(int, input().split()))

dp = [[None] * n for _ in range(n)]
for i in range(len(arr)):
  dp[0][i] = arr[i]


for i in range(1, n):
  larger = (n - i) % 2 == 1
  for j in range(0, n - i):
    if larger:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1])
    else:
      dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1])

print(dp[-1][0])
