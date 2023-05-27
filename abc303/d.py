import math

x, y, z = list(map(int, input().split()))
s = input()

dp = [[None] * (len(s) + 1) for _ in range(2)]

dp[0][0] = math.inf
dp[1][0] = 0

for i in range(1, len(s) + 1):
  c = s[i - 1]
  if c is 'A':
    dp[0][i] = min(dp[0][i - 1] + x, dp[1][i - 1] + z + x)
    dp[1][i] = min(dp[0][i - 1] + z + y, dp[1][i - 1] + y)
  else:
    dp[0][i] = min(dp[0][i - 1] + y, dp[1][i - 1] + z + y)
    dp[1][i] = min(dp[0][i - 1] + z + x, dp[1][i - 1] + x)

print(min(dp[0][-1], dp[1][-1]))
