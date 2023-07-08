n, m = list(map(int, input().split()))
prr = [None] + list(map(int, input().split()))
for i in range(1, n):
  prr[i] -= 1

inss = []
for i in range(m):
  x, y = list(map(int, input().split()))
  inss.append((x - 1, y))

children = [[] for _ in range(n)]
for i in range(1, n):
  children[prr[i]].append(i)

guarded = [False] * n

for i in range(m):
  x, y = inss[i]
