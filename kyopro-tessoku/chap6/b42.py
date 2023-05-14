n = int(input())
arr = []
brr = []
for i in range(n):
  a, b = list(map(int, input().split()))
  arr.append(a)
  brr.append(b)

popo = 0
for i in range(n):
  a, b = arr[i], brr[i]
  if a + b > 0:
    popo += a + b

nepo = 0
for i in range(n):
  a, b = arr[i], brr[i]
  if -a + b > 0:
    nepo += -a + b

pone = 0
for i in range(n):
  a, b = arr[i], brr[i]
  if a - b > 0:
    pone += a - b

nene = 0
for i in range(n):
  a, b = arr[i], brr[i]
  if -a - b > 0:
    nene += -a - b

print(max(popo, nepo, pone, nene))
