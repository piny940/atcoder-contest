from collections import deque

n = int(input())
hrr = list(map(int, input().split()))

costs = [0, abs(hrr[1] - hrr[0])]
prevs = [0, 0]

for i in range(2, n):
  if costs[i - 1] + abs(hrr[i] - hrr[i - 1]) < costs[i - 2] + abs(hrr[i] - hrr[i - 2]):
    costs.append(costs[i - 1] + abs(hrr[i] - hrr[i - 1]))
    prevs.append(i - 1)
  else:
    costs.append(costs[i - 2] + abs(hrr[i] - hrr[i - 2]))
    prevs.append(i - 2)

path = deque([n])
i = n - 1
while i > 0:
  i = prevs[i]
  path.appendleft(i + 1)

print(len(path))
print(*path)
