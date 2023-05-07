n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

cans = [[False] * (s + 1) for i in range(n)]

for i in range(n):
  if i == 0:
    if arr[0] <= s:
      cans[i][arr[0]] = True
    cans[i][0] = True
    continue
  for j in range(s + 1):
    if j < arr[i]:
      cans[i][j] = cans[i - 1][j]
      continue
    cans[i][j] = cans[i - 1][j] or cans[i - 1][j - arr[i]]

print('Yes' if cans[n - 1][s] else 'No')
