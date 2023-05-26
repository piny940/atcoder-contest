n = int(input())
arr = list(map(int, input().split()))
d = int(input())
lrs = []
for _ in range(d):
  l, r = list(map(int, input().split()))
  lrs.append((l - 1, r - 1))

lmaxs = [0] * n
rmaxs = [0] * n

lmaxs[0] = arr[0]
rmaxs[-1] = arr[-1]

for i in range(1, n):
  lmaxs[i] = max(arr[i], lmaxs[i - 1])

for i in reversed(range(0, n - 1)):
  rmaxs[i] = max(arr[i], rmaxs[i + 1])

for i in range(d):
  l, r = lrs[i]
  lmax = 0 if l == 0 else lmaxs[l - 1]
  rmax = 0 if r == n - 1 else rmaxs[r + 1]
  print(max(lmax, rmax))
