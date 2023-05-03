n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))

sums = []
prev = 0
for date in range(n):
  sums.append(prev + arr[date])
  prev = sums[-1]

for i in range(q):
  l, r = list(map(int, input().split()))
  if l == 1:
    print(sums[r-1])
  else:
    print(sums[r-1] - sums[l-2])
