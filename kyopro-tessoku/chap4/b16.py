import math

n = int(input())
hrr = list(map(int, input().split()))

costs = [None] * n

costs[0] = 0
costs[1] = abs(hrr[1] - hrr[0])

for i in range(2, n):
  costs[i] = min(costs[i - 2] + abs(hrr[i] - hrr[i - 2]), costs[i - 1] + abs(hrr[i] - hrr[i - 1]))

print(costs[-1])
