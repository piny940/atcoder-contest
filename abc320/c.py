import math
m = int(input())
s1 = list(map(int, list(input())))
s2 = list(map(int, list(input())))
s3 = list(map(int, list(input())))

answer = math.inf
for i in range(m):
  l1 = s1[i]
  for j in range(m):
    l2 = s2[j]
    for k in range(m):
      l3 = s3[k]
      if l1 != l2 or l2 != l3:
        continue
      if i == j:
        j += m
      if i == k:
        k += m
      if j == k:
        k += m
      t = max(i, j, k)
      answer = min(answer, t)

if answer == math.inf:
  print(-1)
else:
  print(answer)
