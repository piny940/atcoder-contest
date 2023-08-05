n, k = list(map(int, input().split()))
nums = [str(i + 1) for i in range(n)] * 2

sums = []
for i in range(n):

  print('? ' + ' '.join(nums[i:i + k]))
  s = int(input())
  sums.append(s)

ansrr = [None] * n
for i in range(n):
  if i - k + 1 >= 0:
    ansrr[i] = sum(sums[i - k + 1:i + 1]) % 2
  else:
    ansrr[i] = (sum(sums[0:i + 1]) + sum(sums[i - k + 1 + n:n])) % 2

print('! ' + ' '.join(map(str, ansrr)))
