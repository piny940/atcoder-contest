import math
from random import randint


def dis(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def distance(path):
  sum = 0
  current = 0
  for p in path:
    sum += dis(current, p)
    current = p
  sum += dis(current, 0)
  return sum


n = int(input())
points = []
for i in range(n):
  x, y = list(map(int, input().split()))
  points.append((x, y))

current = 0
path = []
yet = [i for i in range(1, n)]
while len(yet) > 0:
  min_dis = math.inf
  next = None
  for p in yet:
    dis = dis(points[p], points[current])
    if dis < min_dis:
      next = p
      min_dis = dis
  path.append(next)
  current = next
  yet.remove(next)


def diff(l, r):
  pl = points[path[l]]
  pr = points[path[r]]
  pll = points[0 if l == 0 else path[l - 1]]
  prr = points[0 if r == n - 2 else path[r + 1]]
  return dis(pll, pr) + dis(pl, prr) - dis(pll, pl) - dis(prr, pr)


min_dis = math.inf
current = 0

for i in range(300000):
  idxes = [randint(0, n - 2), randint(0, n - 2)]
  l, r = min(idxes), max(idxes)
  if diff(l, r) < 0:
    path[l:r + 1] = reversed(path[l:r + 1])

print(1)
for p in path:
  print(p + 1)
print(1)
