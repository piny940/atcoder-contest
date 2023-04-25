n = int(input())
arr = list(map(int, input().split()))

arr.sort()

prev = -1
ans = 0
for color in arr:
  if prev == color:
    ans += 1
    prev = -1
  else:
    prev = color

print(ans)
