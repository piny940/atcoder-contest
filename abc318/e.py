n = int(input())
arr = list(map(int, input().split()))

diffs = {}
blanked = {}
answer = 0

for i in range(1, n + 1):
  diffs[i] = -1
  blanked[i] = False

prev = -1

for i in range(n - 1, -1, -1):
  if arr[i] != prev:
    diffs[arr[i]] += 1
  answer += diffs[arr[i]]

print(answer)
