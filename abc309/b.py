n = int(input())
arr = []
for i in range(n):
  row = list(input())
  arr.append(row)

brr = [[None] * n for _ in range(n)]

brr[0] = [(arr[1][0] if i == 0 else arr[0][i - 1]) for i in range(n)]
brr[n - 1] = [(arr[n - 2][-1] if i == n - 1 else arr[n - 1][i + 1]) for i in range(n)]

for i in range(1, n - 1):
  brr[i][0] = arr[i + 1][0]
  brr[i][n - 1] = arr[i - 1][n - 1]
  for j in range(1, n - 1):
    brr[i][j] = arr[i][j]

for i in range(n):
  print(''.join(brr[i]))
