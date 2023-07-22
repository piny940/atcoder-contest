n, d = list(map(int, input().split()))
sarr = []
for i in range(n):
  s = input()
  sarr.append(s)

ans = 0
seq = 0
for day in range(d):
  free = True
  for i in range(n):
    if sarr[i][day] == 'x':
      free = False
      break
  if free:
    seq += 1
    ans = max(ans, seq)
  else:
    seq = 0

print(ans)
