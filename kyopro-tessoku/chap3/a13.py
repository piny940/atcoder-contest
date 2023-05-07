n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for i in range(len(arr)):
  smaller = arr[i]
  start = i
  end = len(arr)

  # x以下を保ったまま探索する場合はendを含まない配列で考える
  while end - start > 1:
    middle = (start + end) // 2
    if arr[middle] - smaller <= k:
      start = middle
    else:
      end = middle

  ans += start - i

print(ans)
