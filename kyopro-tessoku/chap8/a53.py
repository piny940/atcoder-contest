import heapq

q = int(input())

heap = []
for _ in range(q):
  query = input().split(' ')
  if query[0] == '1':
    heapq.heappush(heap, int(query[1]))
  elif query[0] == '2':
    print(heap[0])
  else:
    heapq.heappop(heap)
