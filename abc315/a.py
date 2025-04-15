s = input()

result = []
for l in s:
  if l not in 'aiueo':
    result.append(l)

print(''.join(result))
