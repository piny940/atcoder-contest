n, q = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

sizes = [1] * n
parents = [None] * n


def get_root(node):
  while parents[node]:
    node = parents[node]
  return node


for num, u, v in queries:
  u -= 1
  v -= 1
  root1 = get_root(u)
  root2 = get_root(v)
  if num == 1:
    if root1 == root2:
      continue
    if sizes[root1] < sizes[root2]:
      parents[root1] = root2
      sizes[root2] += sizes[root1]
    else:
      parents[root2] = root1
      sizes[root1] += sizes[root2]
  else:
    print('Yes' if root1 == root2 else 'No')
