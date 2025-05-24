n, m = list(map(int, input().split()))
larr: list[int] = list(map(int, input().split()))

start = max(larr)
end = sum(larr) + len(larr)

while end - start > 1:
  mid = (start + end) // 2
  # 解がmid-1以下か調べる
  w_limit = mid - 1
  height = 1
  width = 0
  for l in larr:
    if width == 0:
      width += l
    elif width + l + 1 > w_limit:
      width = l
      height += 1
    else:
      width += l + 1
  if height > m:
    # 幅wで収まらない
    start = mid
  else:
    end = mid

print(start)
