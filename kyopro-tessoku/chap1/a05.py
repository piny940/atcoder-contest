n, k = list(map(int, input().split()))

ans = 0

for r in range(1, min(n, k - 2) + 1):
  for b in range (max(1, k - r - n), min(n, k - r - 1) + 1):
    ans += 1

print(ans)

# nを2進数で表したときのj桁目:
# (n // 2**(j-1)) % 2
