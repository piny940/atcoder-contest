n, l = list(map(int, input().split()))
arr = []
brr = []
for i in range(n):
  a, b = input().split(' ')
  arr.append(int(a))
  brr.append(b)

ans = 0
for i in range(n):
  a, b = arr[i], brr[i]
  if b == 'E':
    ans = max(ans, l - arr[i])
  else:
    ans = max(ans, arr[i])

print(ans)
