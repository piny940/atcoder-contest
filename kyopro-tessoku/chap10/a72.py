import copy

h, w, k = list(map(int, input().split()))
crr = []
for _ in range(h):
  row = list(input())
  crr.append(row)

ans = 0
for pattern in range(2**h):
  copied = copy.deepcopy(crr)
  rest = k

  for i in range(h):
    if pattern // 2**i % 2 == 0:
      continue
    for j in range(w):
      copied[i][j] = '#'
    rest -= 1
    if rest == 0:
      break
  black_counts = [0] * w
  for j in range(w):
    for i in range(h):
      if copied[i][j] == '#':
        black_counts[j] += 1
  black_counts.sort()
  count = sum(black_counts[rest:]) + rest * h
  ans = max(ans, count)

print(ans)
