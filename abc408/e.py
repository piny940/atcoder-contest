import math
import heapq
n, m = list(map(int, input().split()))
edges = []

for _ in range(m):
  u, v, w = list(map(int, input().split()))
  edges.append((u - 1, v - 1, w))

adjs = [{} for i in range(n)]
dist = [math.inf] * n
dist[0] = 0

for u, v, w in edges:
  adjs[u].append((v, w))
  adjs[v].append((u, w))

heap = [(0, 0)]
searched = [False] * n

while (len(heap)) > 0:
  current = heapq.heappop(heap)[1]
  if searched[current]:
    continue
  searched[current] = True
  if current == n - 1:
    break
  for adj, w in adjs[current]:
    if dist[current] | w < dist[adj]:
      dist[adj] = dist[current] | w
      heapq.heappush(heap, (dist[adj], adj))

print(dist[n - 1])
