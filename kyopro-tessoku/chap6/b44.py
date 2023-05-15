n = int(input())
arrs = []
for i in range(n):
  arr = list(map(int, input().split()))
  arrs.append(arr)

q = int(input())
queries = []

for i in range(q):
  query = list(map(int, input().split()))
  queries.append((query[0], query[1] - 1, query[2] - 1))

map = [i for i in range(n)]

for (n, x, y) in queries:
  if n == 1:
    map[x], map[y] = map[y], map[x]
  else:
    print(arrs[map[x]][y])
