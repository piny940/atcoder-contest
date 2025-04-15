import sys
import heapq
import os

# 再帰呼び出しの深さの上限を 3000000 に設定
sys.setrecursionlimit(3000000)


H, W = list(map(int, input().split()))
board = []
for i in range(H):
  arr = list(input())
  board.append(arr)

passables = [[True] * W for _ in range(H)]
obs = ['#', '>', '<', '^', 'v']
start = (-1, -1)

for i in range(H):
  for j in range(W):
    a = board[i][j]
    if a in obs:
      passables[i][j] = False
    if a == '>':
      current = j + 1
      while current < W and board[i][current] not in obs:
        passables[i][current] = False
        current += 1
    elif a == '^':
      current = i - 1
      while current >= 0 and board[current][j] not in obs:
        passables[current][j] = False
        current -= 1
    elif a == 'v':
      current = i + 1
      while current < H and board[current][j] not in obs:
        passables[current][j] = False
        current += 1
    elif a == '<':
      current = j - 1
      while current >= 0 and board[i][current] not in obs:
        passables[i][current] = False
        current -= 1
    elif a == 'S':
      start = (i, j)


def passable(y, x):
  if x < 0 or x >= W or y < 0 or y >= H:
    return False
  return passables[y][x]


searched = [[False] * W for _ in range(H)]
found = [(0, start)]

while len(found) > 0:
  cost, (y, x) = heapq.heappop(found)
  searched[y][x] = True
  if board[y][x] == 'G':
    print(cost)
    exit(0)
  if passable(y + 1, x) and not searched[y + 1][x]:
    heapq.heappush(found, (cost + 1, (y + 1, x)))
  if passable(y - 1, x) and not searched[y - 1][x]:
    heapq.heappush(found, (cost + 1, (y - 1, x)))
  if passable(y, x + 1) and not searched[y][x + 1]:
    heapq.heappush(found, (cost + 1, (y, x + 1)))
  if passable(y, x - 1) and not searched[y][x - 1]:
    heapq.heappush(found, (cost + 1, (y, x - 1)))

print(-1)
