a, b = list(map(int, input().split()))

p = a
q = b

while q > 1:
  r = p % q

  if r == 0:
    break
  p = q
  q = r

print(q)
