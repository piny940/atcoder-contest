from collections import deque

q = int(input())
queries = []
for i in range(q):
  query = input().split(' ')
  queries.append(query)

stack = deque()
for query in queries:
  if query[0] == '1':
    stack.append(query[1])
  elif query[0] == '2':
    print(stack[-1])
  else:
    stack.pop()
