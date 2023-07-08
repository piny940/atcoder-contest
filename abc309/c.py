n, k = list(map(int, input().split()))
meds = []
for i in range(n):
  a, b = list(map(int, input().split()))
  meds.append((a, b))

meds.sort(key=lambda m: m[0])

count = sum(map(lambda m: m[1], meds))

if count <= k:
  print(1)
  exit()

for med in meds:
  a, b = med
  count -= b
  if count <= k:
    print(a + 1)
    exit()
