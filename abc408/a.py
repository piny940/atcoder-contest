n, s = list(map(int, input().split()))
trr = list(map(int, input().split()))

if trr[0] > s:
  print('No')
  exit(0)

for i in range(1, n):
  if trr[i] - trr[i - 1] > s:
    print('No')
    exit(0)

print('Yes')
