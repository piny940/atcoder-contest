n, m = list(map(int, input().split()))
amat = []

for i in range(m):
  row = list(map(int, input().split()))
  amat.append(row)

allsets = []
for i in range(n):
  for j in range(i + 1, n):
    allsets.append({i, j})

for i in range(m):
  row = amat[i]
  for j in range(n - 1):
    pair = row[j] - 1, row[j + 1] - 1
    if set(pair) in allsets:
      allsets.remove(set(pair))

print(len(allsets))
