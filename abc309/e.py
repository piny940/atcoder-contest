import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(3000000)

n, m = list(map(int, input().split()))
prr = [None] + list(map(int, input().split()))
for i in range(1, n):
  prr[i] -= 1

inss = []
for i in range(m):
  x, y = list(map(int, input().split()))
  inss.append((x - 1, y))

children = [[] for _ in range(n)]
for i in range(1, n):
  children[prr[i]].append(i)

guarded = [False] * n

ins_rest = [0] * n
count = 0
for x, y in inss:
  ins_rest[x] = max(ins_rest[x], y + 1)


def update(x):
  if ins_rest[x] > 0:
    guarded[x] = True

  for child in children[x]:
    ins_rest[child] = max(ins_rest[child], ins_rest[x] - 1)
    update(child)


update(0)

for i in range(n):
  if guarded[i]:
    count += 1

print(count)
