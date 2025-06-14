n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = -1

for i in range(0, 101):
  trr = arr.copy()
  trr.append(i)
  trr.sort()
  score = 0
  for j in range(1, len(trr) - 1):
    score += trr[j]
  if score >= x:
    result = i
    break

print(result)
