import heapq


n, k = map(int, input().split())
p = list(map(int, input().split()))
que = p[0:k]
print(min(que))
heapq.heapify(que)

for i in range(k, n):
    min = heapq.heappop(que)
    min = max(min, p[i])
    heapq.heappush(que, min)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)
