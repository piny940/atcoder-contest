from ast import Tuple
from typing import Union
from collections import deque

N, M = list(map(int, input().split()))
aarr: list[int] = []
barr: list[int] = []
xarr: list[int] = []
yarr: list[int] = []

for _ in range(M):
  a, b, x, y = list(map(int, input().split()))
  aarr.append(a - 1)
  barr.append(b - 1)
  xarr.append(x)
  yarr.append(y)

# 各人ごとに、「誰を見ているのかと、その人へのdiff」のリスト
lookings: dict[int, list[tuple[int, tuple[int, int]]]] = {}

for i in range(N):
  lookings[i] = []

for i in range(M):
  lookings[aarr[i]].append((barr[i], (xarr[i], yarr[i])))
  lookings[barr[i]].append((aarr[i], (-xarr[i], -yarr[i])))

found = [False] * N
coords: list[tuple[int, int]] = [(0, 0) for _ in range(N)]
queue = deque([0])
found[0] = True

while len(queue) > 0:
  current = queue.popleft()
  for looked, diff in lookings[current]:
    if found[looked]:
      continue
    found[looked] = True
    queue.append(looked)
    coords[looked] = (coords[current][0] + diff[0], coords[current][1] + diff[1])


for i in range(N):
  if found[i]:
    coord = coords[i]
    print(f'{coord[0]} {coord[1]}')
  else:
    print('undecidable')
