n, m = list(map(int, input().split()))
lrr = []
rrr = []

for _ in range(m):
  l, r = list(map(int, input().split()))
  lrr.append(l - 1)
  rrr.append(r - 1)

diffs = [0] * n

for i in range(m):
  l, r = lrr[i], rrr[i]
  diffs[l] += 1
  if r < n - 1:
    diffs[r + 1] -= 1

counts = []
prev = 0

for i in range(n):
  c = prev + diffs[i]
  counts.append(c)
  prev = c

print(min(counts))
