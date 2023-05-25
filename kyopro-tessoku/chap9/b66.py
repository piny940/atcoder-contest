from collections import deque


class UnionFind:
  def __init__(self, n):
    self.n = n
    self.parents = [None] * n
    self.sizes = [1] * n

  def get_root(self, v):
    while self.parents[v] != None:
      v = self.parents[v]
    return v

  def unite(self, u, v):
    rootu = self.get_root(u)
    rootv = self.get_root(v)
    if rootu == rootv:
      return
    if self.sizes[rootu] < self.sizes[rootv]:
      self.parents[rootu] = rootv
      self.sizes[rootv] += self.sizes[rootu]
    else:
      self.parents[rootv] = rootu
      self.sizes[rootu] += self.sizes[rootv]

  def is_united(self, u, v):
    return self.get_root(u) == self.get_root(v)


n, m = list(map(int, input().split()))
lines = []
for i in range(m):
  a, b = list(map(int, input().split()))
  a -= 1
  b -= 1
  lines.append((a, b))
q = int(input())
queries = []
for _ in range(q):
  query = list(map(int, input().split()))
  if len(query) == 2:
    t, x = query
    x -= 1
    queries.append((t, x))
  else:
    t, u, v = query
    u -= 1
    v -= 1
    queries.append((t, u, v))

uf = UnionFind(n)

will_stop = [False] * m
for query in queries:
  if query[0] == 1:
    will_stop[query[1]] = True

for i in range(len(lines)):
  if not will_stop[i]:
    uf.unite(*lines[i])

ans = deque()
for query in reversed(queries):
  if query[0] == 1:
    uf.unite(*lines[query[1]])
  else:
    ans.appendleft(uf.is_united(query[1], query[2]))

for b in ans:
  print('Yes' if b else 'No')
