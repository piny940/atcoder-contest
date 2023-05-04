from bisect import bisect_left

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

half = n // 2
formers = arr[:half]
latters = arr[half:]
former_sums = []
latter_sums = []
for pattern in range(2 ** len(formers)):
  sum = 0
  for i in range(len(formers)):
    if pattern // 2**i % 2:
      sum += formers[i]
  former_sums.append(sum)

for pattern in range(2 ** len(latters)):
  sum = 0
  for i in range(len(latters)):
    if pattern // 2**i % 2:
      sum += latters[i]

  latter_sums.append(sum)

ans = False

latter_sums.sort()

for former in former_sums:
  s = k - former
  idx = bisect_left(latter_sums, s)
  if idx < len(latter_sums) and latter_sums[idx] == s:
    ans = True
    break

print('Yes' if ans else 'No')
