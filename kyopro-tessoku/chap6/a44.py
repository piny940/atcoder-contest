n, q = list(map(int, input().split()))
arr = [i + 1 for i in range(n)]
queries = []

for i in range(q):
  query = list(map(int, input().split()))
  if query[0] == 1 or query[0] == 3:
    query[1] -= 1
  queries.append(query)

rev = False

for i in range(q):
  query = queries[i]
  if query[0] == 1:
    idx = query[1] if not rev else n - query[1] - 1
    arr[idx] = query[2]
  elif query[0] == 2:
    rev = not rev
  else:
    idx = query[1] if not rev else n - query[1] - 1
    print(arr[idx])
