n = int(input())
arr = list(map(int, input().split()))
q = int(input())

hits = []
prev = 0
for i in range(n):
  hits.append(prev + arr[i])
  prev = hits[-1]

for i in range(q):
  l, r = list(map(int, input().split()))
  wins = hits[r-1] - hits[l-2] if l > 1 else hits[r-1]
  if wins > r - l + 1 - wins:
    print('win')
  elif wins == r - l + 1 - wins:
    print('draw')
  else:
    print('lose')
