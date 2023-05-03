t = int(input())
n = int(input())

diffs = [0] * (t+1)
for person in range(n):
  l, r = list(map(int, input().split()))
  diffs[l] += 1
  diffs[r] -= 1

prev = 0
for time in range(t):
  num = prev + diffs[time]
  prev = num
  print(num)
