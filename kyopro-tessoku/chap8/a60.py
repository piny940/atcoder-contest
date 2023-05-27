n = int(input())
arr = list(map(int, input().split()))

stocks = []
ans = []

for i, v in enumerate(arr):
  while len(stocks) > 0:
    if stocks[-1][1] > v:
      break
    stocks.pop()
  if len(stocks) == 0:
    ans.append(-1)
  else:
    ans.append(stocks[-1][0])
  stocks.append((i + 1, v))

print(*ans)
