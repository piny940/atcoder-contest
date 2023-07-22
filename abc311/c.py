import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(3000000)

n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
  arr[i] -= 1

found = [False] * n

searched = [-1] * n
path = []
clear = True


def dfs(point, cycle):
  path.append(point)
  searched[point] = cycle
  found[point] = True
  next = arr[point]
  if searched[next] >= cycle:
    return
  else:
    dfs(next, cycle)


for i in range(n):
  if not found[i]:
    dfs(i, i)
  if clear:
    start_idx = path.index(arr[path[-1]])
    print(len(path[start_idx:]))
    print(*map(lambda x: x + 1, path[start_idx:]))
    exit()
