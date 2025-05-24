n = int(input())

slist = []
for i in range(n + 1):
  found = False
  for j in range(1, 10):
    if n % j != 0:
      continue
    if i % (n // j) == 0:
      slist.append(str(j))
      found = True
      break
  if not found:
    slist.append('-')

print(''.join(slist))
