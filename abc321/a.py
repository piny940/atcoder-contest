nstr = list(input())
prev = int(nstr[0])

result = True

for i in range(1, len(nstr)):
  current = int(nstr[i])
  if prev <= current:
    result = False
    break
  prev = current

if result:
  print('Yes')
else:
  print('No')
