n = int(input())
arr = [None] + list(map(int, input().split()))

for i in range(1, n):
  arr[i] -= 1

direct_subs = [[] for _ in range(n)]
for i in range(1, n):
  direct_subs[arr[i]].append(i)

sub_nums = [None] * n
for i in range(n - 1, -1, -1):
  sub_nums[i] = 0
  for sub in direct_subs[i]:
    sub_nums[i] += sub_nums[sub] + 1

print(*sub_nums)
