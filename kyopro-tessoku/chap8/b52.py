from collections import deque

n, x = list(map(int, input().split()))
x -= 1
a = list(input())
queue = deque([])
queue.append(x)
a[x] = '@'
while len(queue) > 0:
  pos = queue.popleft()
  if pos - 1 >= 0 and a[pos - 1] == '.':
    a[pos - 1] = '@'
    queue.append(pos - 1)
  if pos + 1 < len(a) and a[pos + 1] == '.':
    a[pos + 1] = '@'
    queue.append(pos + 1)

print(''.join(a))
