n = int(input())
s = input()

res1 = [1] * n
for i in range(n - 1):
  if s[i] == 'A':
    res1[i + 1] = res1[i] + 1
  else:
    res1[i + 1] = 1

res2 = [1] * n
for i in reversed(range(1, n)):
  if s[i - 1] == 'B':
    res2[i - 1] = res2[i] + 1
  else:
    res2[i - 1] = 1

ans = 0
for i in range(n):
  ans += max(res1[i], res2[i])

print(ans)
