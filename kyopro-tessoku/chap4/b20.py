# 編集距離(= レーベンシュタイン距離)
s = input()
t = input()

w = len(t) + 1
h = len(s) + 1
dps = [[0] * w for i in range(h)]

for i in range(w):
  dps[0][i] = i

for i in range(h):
  dps[i][0] = i

for i in range(1, h):
  for j in range(1, w):
    cost = 0 if s[i - 1] == t[j - 1] else 1
    dps[i][j] = min(dps[i - 1][j] + 1, dps[i][j - 1] + 1, dps[i - 1][j - 1] + cost)

print(dps[-1][-1])
