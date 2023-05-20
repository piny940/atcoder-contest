import heapq

n, d = list(map(int, input().split()))

jobs = []
for i in range(n):
  x, y = list(map(int, input().split()))
  jobs.append((x - 1, y))

jobs.sort(key=lambda job: job[0])

availables = []
idx = 0
ans = 0
for day in range(d):
  while idx < n and jobs[idx][0] <= day:
    heapq.heappush(availables, -jobs[idx][1])
    idx += 1
  if len(availables) > 0:
    ans -= heapq.heappop(availables)

print(ans)
