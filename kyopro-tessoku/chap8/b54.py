n = int(input())

ans = 0
counts = {}
for i in range(n):
  a = int(input())
  if a in counts:
    ans += counts[a]
    counts[a] += 1
  else:
    counts[a] = 1

print(ans)
