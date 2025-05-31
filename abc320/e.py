import math
from typing import Any

n, m = list(map(int, input().split()))
tarr = []
warr: list[int] = []
sarr: list[int] = []

for _ in range(m):
  t, w, s = list(map(int, input().split()))
  tarr.append(t)
  warr.append(w)
  sarr.append(s)

eaters = [math.inf] * m
eaters[0] = 0

tarr.append(math.inf)


def back_event(back_time):
  start = 0
  end = len(tarr)
  while end - start > 1:
    mid = (start + end) // 2
    if back_time < tarr[mid]:
      end = mid
    else:
      start = mid
  return start


for i in range(m - 1):
  eater = eaters[i]
  eaters[i + 1] = min(eaters[i + 1], eater + 1)

  back_time = tarr[i] + sarr[i]
  back = back_event(back_time)
  if back < m:
    eaters[back] = min(eater, eaters[back])

amounts: list[Any] = [0] * n
for i in range(m):
  eater = eaters[i]
  amount = warr[i]
  amounts[eater] += amount

for a in amounts:
  print(a)
