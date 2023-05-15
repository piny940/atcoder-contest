from functools import cmp_to_key
import heapq
from collections import deque

n, d = list(map(int, input().split()))
jobs = []

for i in range(n):
  x, y = list(map(int, input().split()))
  jobs.append((x, -y))


def cmp_job(j1, j2):
  if j1[0] > j2[0]:
    return 1
  elif j1[0] == j2[0]:
    return 0
  else:
    return -1


sorted_jobs = deque(sorted(jobs, key=cmp_to_key(cmp_job)))
available_jobs = []
heapq.heapify(available_jobs)

ans = 0

for day in range(1, d + 1):
  while True:
    if len(sorted_jobs) == 0:
      break
    job = sorted_jobs[0]
    if day >= job[0]:
      sorted_jobs.popleft()
      heapq.heappush(available_jobs, job[1])
    else:
      break
  if len(available_jobs) > 0:
    revenue = heapq.heappop(available_jobs)
    ans += -revenue

print(ans)
