n, q = list(map(int, input().split()))

queries = []
for _ in range(q):
  query = input().split()
  if query[0] == '1':
    t, u, v = list(map(int, query))
    queries.append((t, u - 1, v - 1))
  else:
    t, v = list(map(int, query))
    queries.append((t, v - 1))

adjs = [set() for _ in range(n)]
ans = n

for query in queries:
  if query[0] == 1:
    u, v = query[1:]
    if len(adjs[u]) == 0:
      ans -= 1
    if len(adjs[v]) == 0:
      ans -= 1
    adjs[u].add(v)
    adjs[v].add(u)
  else:
    v = query[1]
    for u in adjs[v]:
      adjs[u].remove(v)
      if len(adjs[u]) == 0:
        ans += 1
    if len(adjs[v]) != 0:
      ans += 1
    adjs[v] = set()
  print(ans)
