n = int(input())

p = 0
for _ in range(n):
  t, a = input().split(' ')
  a = int(a)
  if t == '+':
    p += a
  elif t == '-':
    p -= a
  else:
    p *= a
  p %= 10000
  print(p % 10000)
