import heapq

n, q = list(map(int, input().split()))

events = []
for i in range(q):
  events.append(list(map(int, input().split())))

uncalled = list(range(1, n+1))
heapq.heapify(uncalled)
called = []
gone = set([])

answer = []

for event in events:
  if event[0] == 1:
    person = heapq.heappop(uncalled)
    heapq.heappush(called, person)
  elif event[0] == 2:
    gone.add(event[1])
  else:
    while True:
      person = called[0]
      if person in gone:
        heapq.heappop(called)
      else:
        answer.append(person)
        break

for p in answer:
  print(p)
