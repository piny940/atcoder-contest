import math


def toBit(set):
  pattern = 0
  for v in set:
    pattern += 2 ** v
  return pattern


def toSet(bit):
  result = set([])
  for i in range(len(bin(bit)) - 2):
    if bit // 2**i % 2:
      result.add(i)
  return result


n, m = list(map(int, input().split()))
amat = []
for i in range(m):
  row = list(map(int, input().split()))
  amat.append(row)

availables = []
for i in range(m):
  items = set()
  for j in range(n):
    if amat[i][j]:
      items.add(j)
  availables.append(items)

counts = [[math.inf] * 2**n for i in range(m)]
counts[0][0] = 0

for pattern in range(1, 2**n):
  if availables[0] >= toSet(pattern):
    counts[0][pattern] = 1

for i in range(m - 1):
  for j in range(2**n):
    counts[i + 1][j] = min(counts[i + 1][j], counts[i][j])
    newSet = availables[i + 1] | toSet(j)
    counts[i + 1][toBit(newSet)] = min(counts[i + 1][toBit(newSet)], counts[i][j] + 1)

print(-1 if counts[-1][-1] == math.inf else counts[-1][-1])
