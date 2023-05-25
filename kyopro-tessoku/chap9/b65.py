import sys
sys.setrecursionlimit(120000)

n, t = list(map(int, input().split()))
t -= 1

adjs = [[] for _ in range(n)]
for i in range(n - 1):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b - 1)
  adjs[b - 1].append(a - 1)

direct_subs = [[] for _ in range(n)]


def check_subs(current, parent):
  for adj in adjs[current]:
    if adj == parent:
      continue
    direct_subs[current].append(adj)
    check_subs(adj, current)


check_subs(t, None)

ranks = [0] * n


def check_rank(current):
  max_rank = 0
  for sub in direct_subs[current]:
    check_rank(sub)
    max_rank = max(max_rank, ranks[sub] + 1)
  ranks[current] = max_rank


check_rank(t)

print(*ranks)
