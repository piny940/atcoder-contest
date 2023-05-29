s = input()
n = int(input())

t = set()

for i in range(2**len(s)):
  istr = bin(i)[2:].zfill(len(s))
  ok = True
  for j in range(len(s)):
    if s[j] is not '?' and s[j] is not istr[j]:
      ok = False
      break
  if ok and i <= n:
    t.add(i)

if len(t) > 0:
  print(max(t))
else:
  print(-1)
