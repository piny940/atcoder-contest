from random import randint

LENGTH = 2
COUNT = 20

for i in range(1, 1 + COUNT):
  srr = []
  for _ in range(LENGTH):
    p = randint(0, 2)
    if p == 2:
      srr.append('?')
    else:
      srr.append(str(p))
  n = randint(0, 2**LENGTH)
  f = open(f'abc301/dsample{i}.txt', mode='w')
  f.writelines([''.join(srr) + '\n', str(n) + '\n'])
  f.close()
