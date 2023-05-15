def gcs(m, n):
  p = m
  q = n
  while q > 1:
    r = p % q
    if r == 0:
      break
    p = q
    q = r
  return q


a, b = list(map(int, input().split()))

g = gcs(a, b)
print(a * b // g)
