import math

n = int(input())
xs, ys, zs = [0], [0], [0]
for i in range(n):
  x, y, z = list(map(int, input().split()))
  xs.append(x)
  ys.append(y)
  zs.append(z)

cost_return = []  # 各選挙区の(あと何人鞍替えする必要があるか, 獲得できる議席数)の配列

for i in range(n + 1):
  x, y, z = xs[i], ys[i], zs[i]
  if x > y:
    cost_return.append((0, z))
  else:
    cost = (y - x + 1) // 2
    cost_return.append((cost, z))

zsum = sum(zs)

dp = [[math.inf] * (zsum + 1) for _ in range(n + 1)]  # 縦: 選挙区番号、横: 獲得議席数、値: 鞍替えする人数
dp[0][0] = 0

for distinct in range(1, n + 1):
  cost, ret = cost_return[distinct]
  for prev in range(zsum + 1):
    if dp[distinct - 1][prev] == math.inf:
      continue

    # 選挙区distinctの議席を獲得する場合
    dp[distinct][prev + ret] = min(dp[distinct][prev + ret], dp[distinct - 1][prev] + cost)

    # 選挙区distinctの議席を獲得しない場合
    dp[distinct][prev] = min(dp[distinct][prev], dp[distinct - 1][prev])

min_cost = math.inf
goal = (zsum + 1) // 2
for cost in dp[n][goal:]:  # 過半数以上の議席を取る場合の中でcostが最小のものを選ぶ
  min_cost = min(min_cost, cost)

print(min_cost)
