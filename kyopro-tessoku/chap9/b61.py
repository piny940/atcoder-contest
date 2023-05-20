import math

n, m = list(map(int, input().split()))

adjs = [[] for _ in range(n)]

for i in range(m):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b)
  adjs[b - 1].append(a)

max = -math.inf
ans = None

for i in range(n):
  if len(adjs[i]) > max:
    max = len(adjs[i])
    ans = i

print(ans + 1)
