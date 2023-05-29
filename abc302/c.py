import itertools

n, m = list(map(int, input().split()))
srr = []

for _ in range(n):
  srr.append(input())

srrall = itertools.permutations(srr)

ans = False
for trr in srrall:
  result = True
  for i in range(n - 1):
    t1 = trr[i]
    t2 = trr[i + 1]
    diff = 0
    for j in range(m):
      if t1[j] != t2[j]:
        diff += 1
    if diff > 1:
      result = False
      break
  if result:
    ans = True
    break

print('Yes' if ans else 'No')
