from collections import deque

n, m = list(map(int, input().split()))
edges: list[tuple[int, int, int]] = []

for _ in range(m):
  a, b, w = list(map(int, input().split()))
  edges.append((a - 1, b - 1, w))

adjs: list[list[tuple[int, int]]] = [[] for _ in range(n)]
for a, b, w in edges:
  adjs[a].append((b, w))


visited = [[False] * 1024 for _ in range(n)]

queue = deque([(0, 0)])

while len(queue) > 0:
  current, xor = queue.popleft()
  for adj, w in adjs[current]:
    if not visited[adj][xor ^ w]:
      queue.append((adj, xor ^ w))
      visited[adj][xor ^ w] = True

exist = False
for xor in range(1024):
  if visited[-1][xor]:
    print(xor)
    exist = True
    break

if not exist:
  print(-1)
