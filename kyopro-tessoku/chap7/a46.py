import math


def sqdis(p1, p2):
  return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


n = int(input())
points = []
for i in range(n):
  x, y = list(map(int, input().split()))
  points.append((x, y))

current = 0
path = [0]
yet = [i for i in range(1, n)]
while len(yet) > 0:
  min = math.inf
  next = None
  for p in yet:
    dis = sqdis(points[p], points[current])
    if dis < min:
      next = p
      min = dis
  path.append(next)
  current = next
  yet.remove(next)

path.append(0)

for p in path:
  print(p + 1)
