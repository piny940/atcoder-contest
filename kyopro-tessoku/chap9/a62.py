import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

n, m = list(map(int, input().split()))

adjs = [[] for _ in range(n)]

for i in range(m):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b - 1)
  adjs[b - 1].append(a - 1)

searched = [False] * n


def dfs(current):
  searched[current] = True
  for adj in adjs[current]:
    if not searched[adj]:
      dfs(adj)


dfs(0)
print('The graph is connected.' if all(searched) else ' The graph is not connected.')
