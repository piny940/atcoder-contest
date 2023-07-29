n, m = list(map(int, input().split()))
srr = []
for i in range(n):
  s = input()
  srr.append(s)

results = []


def check(x, y):
  result = True
  for i in range(0, 3):
    for j in range(0, 3):
      result = srr[x + i][y + j] == srr[x + 8 - i][y + 8 - j] == '#'
      if not result:
        return False
  for i in range(0, 4):
    result = srr[x + 3][y + i] == srr[x + i][y + 3] == srr[x + 5][y + 8 - i] == srr[x + 8 - i][y + 5] == '.'
    if not result:
      return False
  return True


for i in range(n - 9 + 1):
  for j in range(m - 9 + 1):
    if check(i, j):
      results.append((i, j))

for (x, y) in results:
  print(x + 1, y + 1)
