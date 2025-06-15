import math
n, q = list(map(int, input().split()))
xrr = list(map(int, input().split()))

box = [0] * n
ans = [-1] * q


for i in range(q):
  x = xrr[i]
  if x >= 1:
    box[x - 1] += 1
    ans[i] = x
  else:
    minidx = 0
    tmpmin = math.inf

    for j in range(len(box)):
      if tmpmin > box[j]:
        minidx = j
        tmpmin = box[j]
    box[minidx] += 1
    ans[i] = minidx + 1

print(' '.join(map(str, ans)))
