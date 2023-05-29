import copy

s = input()
n = int(input())

nstr = list(bin(n)[2:].zfill(len(s)))
s = list(s.zfill(len(nstr)))
t = copy.copy(s)
ans = True
back = -1
for i in range(len(s)):
  if s[i] == nstr[i]:
    continue
  if s[i] == '0' and nstr[i] == '1':
    break
  if s[i] == '?':
    t[i] = nstr[i]
    continue
  back = i - 1
  while True:
    if back < 0:
      ans = False
      break
    if s[back] == '?' and t[back] == '1':
      t[back] = '0'
      break
    back -= 1
  break

if not ans:
  print(-1)
  exit()

if back is not -1:
  for i in range(back + 1, len(s)):
    if s[i] is '?':
      t[i] = '1'
    else:
      t[i] = s[i]

for i in range(len(t)):
  if t[i] == '?':
    t[i] = '1'

print(int(''.join(t), 2))
