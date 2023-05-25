from collections import deque

n, m = list(map(int, input().split()))

adjs = [[] for _ in range(n)]
for i in range(m):
  a, b = list(map(int, input().split()))
  adjs[a - 1].append(b - 1)
  adjs[b - 1].append(a - 1)

queue = deque([0])
counts = [-1] * n
counts[0] = 0
while len(queue) > 0:
  current = queue.popleft()
  for adj in adjs[current]:
    if counts[adj] < 0:
      counts[adj] = counts[current] + 1
      queue.append(adj)

for count in counts:
  print(count)
