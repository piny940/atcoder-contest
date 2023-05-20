q = int(input())

diction = {}
for _ in range(q):
  query = input().split(' ')
  if query[0] == '1':
    diction[query[1]] = int(query[2])
  else:
    print(diction[query[1]])
