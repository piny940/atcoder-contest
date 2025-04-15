import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(3000000)

n = int(input())
cs = []
pss = []

for i in range(n):
  l = list(map(int, input().split()))
  cs.append(l[0])
  pss.append(l[1:])

for i in range(len(pss)):
  for j in range(len(pss[i])):
    p = pss[i][j]
    pss[i][j] = p - 1

order = []
read = [False for i in range(n)]


def search(current: int):
  if read[current]:
    return
  for p in pss[current]:
    search(p)
  if not read[current]:
    order.append(current + 1)
    read[current] = True


search(0)
order = order[:-1]  # 1は除く

print(' '.join(map(str, order)))
