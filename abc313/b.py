n, m = list(map(int, input().split()))
comprr = []
for _ in range(m):
  a, b = list(map(int, input().split()))
  comprr.append((a - 1, b - 1))

parents = [[] for _ in range(n)]
for a, b in comprr:
  parents[b].append(a)

pro = None
only = True
for i, prr in enumerate(parents):
  if len(prr) is 0:
    if pro is None:
      pro = i
    else:
      only = False

print(pro + 1 if only else -1)
