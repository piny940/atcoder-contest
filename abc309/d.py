import math
import heapq

n1, n2, m = list(map(int, input().split()))
ads = [[] for _ in range(n1 + n2)]
for i in range(m):
  a, b = list(map(int, input().split()))
  a -= 1
  b -= 1
  ads[a].append(b)
  ads[b].append(a)

dist1 = [math.inf] * (n1 + n2)
dist1[0] = 0


def dikstra(start, graph):
  n = len(graph)
  heap = [(0, start)]
  dist = [math.inf] * n
  dist[start] = 0
  searched = [False] * n
  while len(heap) > 0:
    current = heapq.heappop(heap)[1]
    if searched[current]:
      continue
    searched[current] = True
    for adj in ads[current]:
      if dist[current] + 1 < dist[adj]:
        dist[adj] = dist[current] + 1
        heapq.heappush(heap, (dist[adj], adj))
  return dist


def max_index(arr):
  idx = None
  v = -math.inf
  for i in range(len(arr)):
    if arr[i] >= v:
      idx = i
  return idx


dist1 = dikstra(0, ads)
dist2 = dikstra(n1 + n2 - 1, ads)

print(max(dist1[:n1]) + max(dist2[n1:]) + 1)
