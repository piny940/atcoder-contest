n, Q = list(map(int, input().split()))

rotated = 0
arr = [i + 1 for i in range(n)]

for _ in range(Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    _, p, x = query
    arr[(p - 1 + rotated) % n] = x
  elif query[0] == 2:
    _, p = query
    print(arr[(p - 1 + rotated) % n])
  else:
    _, k = query
    rotated += k
    rotated %= n
