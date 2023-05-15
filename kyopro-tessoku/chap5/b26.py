n = int(input())

judges = [True] * (n + 1)

for i in range(2, n + 1):
  if not judges[i]:
    continue

  kake = 2
  while i * kake <= n:
    judges[i * kake] = False
    kake += 1

for i in range(2, n + 1):
  if judges[i]:
    print(i)
