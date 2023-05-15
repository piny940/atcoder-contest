n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
  arr[i] -= 1

MAX_LENGTH = 100
sorted_arr = sorted(arr)
counts = [0] * 100
idx = 0
for length in range(MAX_LENGTH):
  while idx < len(arr) and sorted_arr[idx] == length:
    counts[length] += 1
    idx += 1

ans = 0
for count in counts:
  ans += count * (count - 1) * (count - 2) // 6

print(ans)
