from collections import deque

r, c = list(map(int, input().split()))
start = list(map(int, input().split()))
goal = list(map(int, input().split()))
start[0], start[1] = start[0] - 1, start[1] - 1
goal[0], goal[1] = goal[0] - 1, goal[1] - 1

maze = []
for i in range(r):
  row = input()
  maze.append(row)

queue = deque([start])
distances = [[-1] * c for i in range(r)]
distances[start[0]][start[1]] = 0

while len(queue) > 0:
  y, x = queue.popleft()
  if (y, x) == goal:
    break

  if maze[y][x - 1] == '.' and distances[y][x - 1] < 0:
    queue.append((y, x - 1))
    distances[y][x - 1] = distances[y][x] + 1
  if maze[y][x + 1] == '.' and distances[y][x + 1] < 0:
    queue.append((y, x + 1))
    distances[y][x + 1] = distances[y][x] + 1
  if maze[y - 1][x] == '.' and distances[y - 1][x] < 0:
    queue.append((y - 1, x))
    distances[y - 1][x] = distances[y][x] + 1
  if maze[y + 1][x] == '.' and distances[y + 1][x] < 0:
    queue.append((y + 1, x))
    distances[y + 1][x] = distances[y][x] + 1

print(distances[goal[0]][goal[1]])
