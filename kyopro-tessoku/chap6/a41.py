n = int(input())
s = input()

color = ''
seq = 0
ans = False
for i in range(len(s)):
  if color == s[i]:
    seq += 1
    if seq == 3:
      ans = True
      break
  else:
    color = s[i]
    seq = 1

print('Yes' if ans else 'No')
