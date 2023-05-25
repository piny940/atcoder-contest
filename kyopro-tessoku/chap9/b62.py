import sys

sys.setrecursionlimit(120000)

n, m = list(map(int, input().split()))
adjs = [[] for i in range(n)]
for i in range(m):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b - 1)
  adjs[b - 1].append(a - 1)

searched = [False] * n
searched[0] = True
path = [1]


def dfs(current):
  result = False
  for adj in adjs[current]:
    if adj == n - 1:
      path.append(adj + 1)
      result = True
      break
    if not searched[adj]:
      searched[adj] = True
      path.append(adj + 1)
      result = dfs(adj)
      if result:
        break
      searched[adj] = False
      path.pop()
  return result


dfs(0)
print(*path)
