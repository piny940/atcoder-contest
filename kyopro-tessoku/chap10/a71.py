n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr.sort()
brr.sort(reverse=True)

ans = 0

for i in range(n):
  ans += arr[i] * brr[i]

print(ans)
