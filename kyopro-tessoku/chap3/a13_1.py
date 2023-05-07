n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0

idx = 0
for i in range(n):
  while idx < n and arr[idx] - arr[i] <= k:
    idx += 1
  ans += idx - 1 - i

print(ans)
