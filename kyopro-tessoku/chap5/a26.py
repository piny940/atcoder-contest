import math

q = int(input())

for i in range(q):
  x = int(input())
  if x == 1:
    print('No')
    continue

  ans = True
  wari = 2
  while wari ** 2 <= x:
    if x % wari == 0:
      ans = False
      break
    wari += 1
  print('Yes' if ans else 'No')
