MOD = 100
n = int(input())
arr = list(map(int, input().split()))

counts = [0] * MOD
for num in arr:
  counts[num % MOD] += 1

ans = 0

for i in range(MOD // 2 + 1):
  count = counts[i]
  if i == 0 or i == 50:
    ans += count * (count - 1) // 2
  else:
    other_count = counts[MOD - i]
    ans += count * other_count

print(ans)
