n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

dp = []
for i in range(n + 1):
  result = False
  for j in range(k):
    if i >= arr[j] and dp[i - arr[j]] == False:
      result = True
      break
  dp.append(result)

print('First' if dp[-1] else 'Second')
