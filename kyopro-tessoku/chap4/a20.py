s = input()
t = input()

w = len(s) + 1
h = len(t) + 1
dps = [[0] * w for i in range(h)]

for i in range(w):
  dps[0][i] = 0

for i in range(h):
  dps[i][0] = 0

for i in range(1, h):
  for j in range(1, w):
    if t[i - 1] == s[j - 1]:
      dps[i][j] = max(dps[i - 1][j], dps[i][j - 1], dps[i - 1][j - 1] + 1)
    else:
      dps[i][j] = max(dps[i - 1][j], dps[i][j - 1])

print(dps[-1][-1])
