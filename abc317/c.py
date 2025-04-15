import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(3000000)

n, m = list(map(int, input().split()))
edges = []
for i in range(m):
  a, b, c = list(map(int, input().split()))
  edges.append((a - 1, b - 1, c))

neighbors = [[] for i in range(n)]
for a, b, c in edges:
  neighbors[a].append((b, c))
  neighbors[b].append((a, c))

found = [False for _ in range(n)]
searched = [False for _ in range(n)]
answer = 0


def search(current):
  found[current] = True
  max_cost = 0
  for neighbor, c in neighbors[current]:
    if found[neighbor]:
      continue
    cost = search(neighbor)
    if cost + c > max_cost:
      max_cost = cost + c
  found[current] = False
  return max_cost


for start in range(n):
  answer = max(search(start), answer)

print(answer)
