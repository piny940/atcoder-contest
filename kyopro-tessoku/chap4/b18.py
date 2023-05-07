from collections import deque

n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

cans = [[False] * (s + 1) for i in range(n)]

for i in range(n):
  if i == 0:
    cans[0][0] = True
    if arr[0] <= s:
      cans[0][arr[0]] = True
    continue
  for j in range(s + 1):
    if j < arr[i]:
      cans[i][j] = cans[i - 1][j]
      continue
    cans[i][j] = cans[i - 1][j] or cans[i - 1][j - arr[i]]

if not cans[-1][s]:
  print(-1)
  exit()

choices = deque([])

rest = s
for i in reversed(range(n)):
  if i == 0:
    if rest == arr[0]:
      choices.appendleft(1)
    continue
  if rest < arr[i]:
    continue
  if cans[i - 1][rest - arr[i]]:
    choices.appendleft(i + 1)
    rest -= arr[i]

print(len(choices))
print(*choices)
