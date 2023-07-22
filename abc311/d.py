import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(3000000)

n, m = list(map(int, input().split()))
sarr = []
for i in range(n):
  s = input()
  sarr.append(s)

searched = [[False] * m for _ in range(n)]
directions = ['left', 'right', 'top', 'down']


def in_maze(point):
  return 0 <= point[1] <= m - 1 and 0 <= point[0] <= n - 1


def is_ice(point):
  return in_maze(point) and sarr[point[0]][point[1]] == '.'


def one_next(point, direction):
  if direction == 'top':
    return (point[0] - 1, point[1])
  elif direction == 'down':
    return (point[0] + 1, point[1])
  elif direction == 'left':
    return (point[0], point[1] - 1)
  else:
    return (point[0], point[1] + 1)


def two_next(point, direction):
  return one_next(one_next(point, direction), direction)


def is_to_search(point):
  return is_ice(point) and not searched[point[0]][point[1]]


def to_proceed(point, direction):
  next = one_next(point, direction)
  while is_ice(next):
    if is_to_search(next):
      return True
    else:
      next = one_next(next, direction)
  return False


def debug():
  for i in range(n):
    s = ['T' if searched[i][j] else 'F' for j in range(m)]
    print(''.join(s))
  print("\n")


def dfs(point, direction):
  searched[point[0]][point[1]] = True

  next = one_next(point, direction)

  if is_ice(next):
    if to_proceed(point, direction):
      dfs(next, direction)
    return

  # nextが岩だった場合
  debug()
  for direction in directions:
    next = one_next(point, direction)
    if to_proceed(point, direction):
      dfs(next, direction)


point = (1, 1)
searched[1][1] = True
for direction in directions:
  next = one_next(point, direction)
  if to_proceed(point, direction):
    dfs(next, direction)

count = 0
for i in range(n):
  for j in range(m):
    if searched[i][j]:
      count += 1

print(count)
