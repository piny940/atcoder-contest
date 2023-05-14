from collections import deque

x, y = list(map(int, input().split()))

answers = deque([])

while (x, y) != (1, 1):
  answers.appendleft((x, y))
  if x > y:
    x = x - y
  else:
    y = y - x

print(len(answers))
for tupple in answers:
  print(*tupple)
