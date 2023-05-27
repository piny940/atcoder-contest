import bisect

n, m, h, k = list(map(int, input().split()))
s = input()

items = []
for i in range(m):
  x, y = list(map(int, input().split()))
  items.append([x, y, i])

items = sorted(items)
used = [False] * m

current = [0, 0]
power = h
ans = True
for c in s:
  power -= 1
  if power < 0:
    ans = False
    break
  if c is 'R':
    current[0] += 1
  elif c is 'L':
    current[0] -= 1
  elif c is 'U':
    current[1] += 1
  else:
    current[1] -= 1
  idx = bisect.bisect_left(items, current)

  if power < k and idx < len(items) and not used[items[idx][2]] and items[idx][:2] == current:
    used[items[idx][2]] = True
    power = k

print('Yes' if ans else 'No')
