from collections import deque

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr = [0] + arr
brr = [0, 0] + brr

prevs = [0] * n
costs = [0, arr[1]]

for i in range(2, n):
  if costs[i - 1] + arr[i] > costs[i - 2] + brr[i]:
    prevs[i] = i - 2
    costs.append(costs[i - 2] + brr[i])
  else:
    prevs[i] = i - 1
    costs.append(costs[i - 1] + arr[i])

path = deque([n])
i = n - 1
while i > 0:
  i = prevs[i]
  path.appendleft(i + 1)

print(len(path))
print(*path)
