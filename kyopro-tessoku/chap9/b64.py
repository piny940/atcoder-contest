import heapq
import math
from collections import deque

n, m = list(map(int, input().split()))

adjs = [[] for _ in range(n)]
for i in range(m):
  a, b, c = list(map(int, input().split()))
  adjs[a - 1].append((b - 1, c))
  adjs[b - 1].append((a - 1, c))

found = [(0, 0)]  # (node, distance)
searched = [False] * n
prevs = [None] * n
distances = [math.inf] * n

while len(found) > 0:
  distance, current = heapq.heappop(found)
  if searched[current]:
    continue
  searched[current] = True
  for (adj, cost) in adjs[current]:
    if distances[adj] > distance + cost:
      prevs[adj] = current
      distances[adj] = distance + cost
      heapq.heappush(found, (distance + cost, adj))

path = deque()
current = n - 1
while current != 0:
  path.appendleft(current + 1)
  current = prevs[current]

path.appendleft(1)

print(*path)
