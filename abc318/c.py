n, d, p = list(map(int, input().split()))
fs = list(map(int, input().split()))

fs.sort(reverse=True)

answer = 0

current = 0
while current < n:
  idx = current
  tmp_sum = 0
  for i in range(d):
    if idx + i >= n:
      break
    tmp_sum += fs[idx + i]
  if tmp_sum > p:
    answer += p
  else:
    answer += tmp_sum
  current += d

print(answer)
