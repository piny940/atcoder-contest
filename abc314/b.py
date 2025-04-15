import math

n = int(input())
cs = []
arrs = []
for i in range(n):
  cs.append(int(input()))
  arrs.append(list(map(int, input().split())))

x = int(input())

minc = math.inf
answerers = []

for i in range(n):
  if x not in arrs[i]:
    continue
  if minc < cs[i]:
    continue
  if minc == cs[i]:
    answerers.append(i + 1)
  else:
    answerers = [i + 1]
    minc = cs[i]

print(len(answerers))
print(" ".join(map(str, answerers)))
