n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count = 0

for a in arr:
  if k <= a:
    count += 1

print(count)
