d, n = list(map(int, input().split()))
lrr = []
rrr = []
hrr = []
for i in range(n):
  l, r, h = list(map(int, input().split()))
  lrr.append(l - 1)
  rrr.append(r - 1)
  hrr.append(h)

times = [24] * d

for i in range(n):
  for j in range(lrr[i], rrr[i] + 1):
    times[j] = min(times[j], hrr[i])

sum = 0
for time in times:
  sum += time

print(sum)
