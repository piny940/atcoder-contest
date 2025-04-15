n = int(input())
s = input()
q = int(input())
ts, xs, cs = [], [], []
for i in range(q):
  t, x, c = input().split(' ')
  ts.append(int(t))
  xs.append(int(x) - 1)
  cs.append(c)

last_change_idx = q
last_size = None

for i in range(len(ts)):
  t = ts[i]
  if t == 2:
    last_change_idx = i
    last_size = 'little'
  elif t == 3:
    last_change_idx = i
    last_size = 'large'

result = list(s)
for i in range(last_change_idx):
  if ts[i] != 1:
    continue
  result[xs[i]] = cs[i]

for i in range(len(result)):
  if last_size == 'little':
    result[i] = result[i].lower()
  elif last_size == 'large':
    result[i] = result[i].upper()

for i in range(last_change_idx, q):
  if ts[i] != 1:
    continue
  result[xs[i]] = cs[i]

print(''.join(result))
