n = int(input())
arr = list(map(int, input().split()))

arr.sort()
s = sum(arr)
p, r = s // n, s % n
brr = [p] * (n - r) + [p + 1] * r

count = 0
for i in range(n):
  count += abs(arr[i] - brr[i])
count //= 2

print(count)
