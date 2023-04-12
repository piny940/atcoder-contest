import heapq

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
q = [0]
heapq.heapify(q)
ans = []
k += 1

while len(ans) != k:
  min = heapq.heappop(q)
  while len(ans) != 0 and ans[-1] == min:
    min = heapq.heappop(q)
  
  ans.append(min)
  for price in arr:
    heapq.heappush(q, min + price)

print(ans[-1])
