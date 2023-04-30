d = int(input())
n = int(input())

diffs = [0] * d

for i in range(n):
  l, r = list(map(int, input().split()))
  diffs[l-1] += 1
  if r < d:
    diffs[r] -= 1

prev = 0
for date in range(d):
  num = prev + diffs[date]
  prev = num
  print(num)
