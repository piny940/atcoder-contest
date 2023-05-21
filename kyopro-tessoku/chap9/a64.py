import math
import heapq

n, m = list(map(int, input().split()))
adjs = [[] for i in range(n)]

for i in range(m):
  a, b, c = list(map(int, input().split()))
  a -= 1
  b -= 1
  adjs[a].append((b, c))
  adjs[b].append((a, c))

dist = [math.inf] * n
dist[0] = 0

heap = [(0, 0)]
searched = [False] * n

while len(heap) > 0:
  current = heapq.heappop(heap)[1]
  if searched[current]:
    continue
  searched[current] = True
  for adj, distance in adjs[current]:
    if dist[current] + distance < dist[adj]:
      dist[adj] = dist[current] + distance
      heapq.heappush(heap, (dist[adj], adj))

for cost in dist:
  print(-1 if cost == math.inf else cost)
