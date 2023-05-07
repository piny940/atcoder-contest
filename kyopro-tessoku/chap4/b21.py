n = int(input())
s = input()

dps = [[None] * n for i in range(n)]

for i in range(n):
  dps[i][i] = 1

for i in range(0, n - 1):
  dps[i][i + 1] = 2 if s[i] == s[i + 1] else 1

for r in range(2, n):
  dps[0][r] = dps[0][r - 1]

for layer in range(2, n):
  for l in range(0, n - layer):
    r = l + layer
    if s[l] == s[r]:
      dps[l][r] = max(dps[l + 1][r], dps[l][r - 1], dps[l + 1][r - 1] + 2)
    else:
      dps[l][r] = max(dps[l + 1][r], dps[l][r - 1])

print(dps[0][-1])
