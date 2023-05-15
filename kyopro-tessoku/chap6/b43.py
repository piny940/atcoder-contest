n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(len(arr)):
  arr[i] -= 1
fails = [0] * n

for st in arr:
  fails[st] += 1

for fail in fails:
  print(m - fail)
