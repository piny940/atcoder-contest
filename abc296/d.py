import math


n, m = list(map(int, input().split()))

ans = math.inf

for a in range(1, n + 1):
  b = math.ceil(m / a)
  if b > n: continue
  if a > b: break
  ans = min(ans, a * b)

print(-1 if ans == math.inf else ans)
