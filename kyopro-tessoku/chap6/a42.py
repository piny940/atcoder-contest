from math import floor, ceil

MAX_POWER = 100
MAX_MOTIV = 100


n, k = list(map(int, input().split()))
arr = []
brr = []

for i in range(n):
  a, b = list(map(int, input().split()))
  arr.append(a)
  brr.append(b)

ans = 0
for power in range(1, MAX_POWER + 1):
  for motiv in range(1, MAX_MOTIV + 1):
    tmp = 0
    for st in range(n):
      a, b = arr[st], brr[st]
      if power - floor(k / 2) <= a <= power + ceil(k / 2) and motiv - floor(k / 2) <= b <= motiv + ceil(k / 2):
        tmp += 1
    ans = max(ans, tmp)

print(ans)
