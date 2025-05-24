n, m = map(int, input().split())
larr = list(map(int, input().split()))

start = max(larr) - 1  # 最小でも最長の単語を表示する幅が必要
end = sum(larr) + (n - 1) + 1

while end - start > 1:
  mid = (start + end) // 2
  height = 1
  width = 0
  for l in larr:
    if width == 0:
      width = l
    elif width + 1 + l <= mid:
      width += 1 + l
    else:
      height += 1
      width = l
  if height <= m:
    end = mid
  else:
    start = mid

print(end)
