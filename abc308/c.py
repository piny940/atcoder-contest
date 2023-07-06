from functools import cmp_to_key

n = int(input())

abs = []
for i in range(n):
  a, b = list(map(int, input().split()))
  abs.append((a, b))

pros = [i for i in range(n)]


def comp(u, v):
  uv = abs[u][0] * (abs[v][0] + abs[v][1])
  vv = abs[v][0] * (abs[u][0] + abs[u][1])
  if uv > vv:
    return -1
  elif uv == vv:
    return 0
  else:
    return 1


pros.sort(key=cmp_to_key(comp))

ans = [v + 1 for v in pros]
print(*ans)
