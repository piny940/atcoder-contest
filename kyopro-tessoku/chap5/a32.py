n, a, b = list(map(int, input().split()))

dps = []

for i in range(n + 1):
  if i >= a and dps[i - a] == False:
    dps.append(True)
  elif i >= b and dps[i - b] == False:
    dps.append(True)
  else:
    dps.append(False)

print('First' if dps[-1] else 'Second')
