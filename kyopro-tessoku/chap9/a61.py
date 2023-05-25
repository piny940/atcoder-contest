n, m = list(map(int, input().split()))

adjs = [[] for _ in range(n)]

for i in range(m):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b)
  adjs[b - 1].append(a)

for i in range(n):
  print(f'{i + 1}: {{{", ".join(map(str, adjs[i]))}}}')
