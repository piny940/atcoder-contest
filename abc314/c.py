n, m = list(map(int, input().split()))
s = input()
cs = list(map(int, input().split()))

ps = []
for i in range(m):
  ps.append([])

for pos in range(n):
  letter = s[pos]
  color = cs[pos] - 1
  ps[color].append((pos, letter))

result = ['' for i in range(n)]

for color in range(m):
  for i in range(len(ps[color])):
    pos, letter = ps[color][i]
    new_pos = None
    if i == len(ps[color]) - 1:
      new_pos = ps[color][0][0]
    else:
      new_pos = ps[color][i + 1][0]
    result[new_pos] = letter

print(''.join(result))
