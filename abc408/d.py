import math
t = int(input())

for _ in range(t):
  n = int(input())
  s = list(input())

  preone = [0] * n
  preone[0] = 0 if s[0] == '0' else 1
  for i in range(1, n):
    preone[i] = preone[i - 1] + (0 if s[i] == '0' else 1)

  total_1 = preone[n - 1]
  min_ops = n

preone.append(0)


def minops(start, end):
  if end - start < 1:
    return 0
  mid = (start + end) // 2
  l = minops(start, mid)
  r = minops(mid, end)
  result = math.inf

  # 右側を0埋めする場合
  result = min(result, l + (preone[end - 1] - preone[mid - 1]))

  # 左側を0埋めする場合
  result = min(result, r + (preone[mid - 1] - preone[start - 1]))
