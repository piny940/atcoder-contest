import math

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

for i in range(n - 1):
  arr[i] -= 1
  brr[i] -= 1

scores = [-math.inf] * n

scores[0] = 0

for i in range(n - 1):
  scores[arr[i]] = max(scores[arr[i]], scores[i] + 100)
  scores[brr[i]] = max(scores[brr[i]], scores[i] + 150)

print(scores[-1])
