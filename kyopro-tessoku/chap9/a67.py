class UnionFind:
  def __init__(self, n):
    self.parents = [None] * n
    self.sizes = [1] * n
  
  def get_root(self, v):
    while self.parents[v] is not None:
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
edges = []
for _ in range(m):
  a, b, c = list(map(int, input().split()))
  edges.append((a - 1, b - 1, c))

edges = sorted(edges, key=lambda x: x[2])
uf = UnionFind(n)

ans = 0
for a, b, c in edges:
  if uf.is_united(a, b):
    continue
  uf.unite(a, b)
  ans += c

print(ans)
