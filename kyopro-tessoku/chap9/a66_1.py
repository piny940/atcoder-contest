class UnionFind:
  def __init__(self, n):
    self.n = n
    self.parents = [None] * (n + 1)
    self.sizes = [1] * (n + 1)

  def get_root(self, v):
    while self.parents[v] != None:
      v = self.parents[v]
    return v

  def unite(self, u, v):
    root1 = self.get_root(u)
    root2 = self.get_root(v)
    if root1 == root2:
      return
    if self.sizes[root1] < self.sizes[root2]:
      self.parents[root1] = root2
      self.sizes[root2] += self.sizes[root1]
    else:
      self.parents[root2] = root1
      self.sizes[root1] += self.sizes[root2]

  def same(self, u, v):
    return self.get_root(u) == self.get_root(v)


n, q = list(map(int, input().split()))
queries = []
for _ in range(q):
  t, u, v = list(map(int, input().split()))
  queries.append((t, u - 1, v - 1))


uf = UnionFind(n)
for t, u, v in queries:
  if t == 1:
    uf.unite(u, v)
  else:
    print('Yes' if uf.same(u, v) else 'No')
