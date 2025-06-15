n, h, m = list(map(int, input().split()))
enemies: list[tuple[int, int]] = []

for _ in range(n):
  a, b = list(map(int, input().split()))
  enemies.append((a, b))

dp = [[-1] * (h + 1) for _ in range(n + 1)]

dp[0][h] = m

result = 0

for i in range(1, n + 1):
  a, b = enemies[i - 1]
  defeats = False

  for hp in range(h + 1):
    mp = dp[i - 1][hp]
    if mp == -1:
      continue
    if hp >= a:
      dp[i][hp - a] = max(dp[i][hp - a], dp[i - 1][hp])
      defeats = True
    if mp >= b:
      dp[i][hp] = max(dp[i][hp], dp[i - 1][hp] - b)
      defeats = True
  if not defeats:
    break
  else:
    result += 1

print(result)
