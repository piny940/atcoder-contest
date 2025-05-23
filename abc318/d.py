n = int(input())
m = n * (n - 1) // 2  # edge数
edges = [(-1, -1, -1)]

for i in range(n - 1):
  ds = list(map(int, input().split()))
  for j in range(len(ds)):
    edges.append((i, i + j + 1, ds[j]))

dp = [[0] * 2**n for _ in range(m + 1)]  # 縦: 辺番号、横: 使用済みの頂点を表す01列、値: それまでに選んだ辺の重みの合計


def picked(bit, k):
  return (bit >> k) % 2 == 1


for i in range(len(dp[0])):
  dp[0][i] = 0

for edge_id in range(1, m + 1):
  for prev in range(1 << n):
    u, v, d = edges[edge_id]
    # 辺を選ばない場合
    dp[edge_id][prev] = max(dp[edge_id][prev], dp[edge_id - 1][prev])

    # 辺を選ぶ場合
    if not picked(prev, u) and not picked(prev, v):
      bit = prev + (1 << u) + (1 << v)
      dp[edge_id][bit] = max(dp[edge_id][bit], dp[edge_id - 1][prev] + d)

print(max(dp[m]))
