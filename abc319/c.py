import itertools

carr: list[int] = []

for _ in range(3):
  row = list(map(int, input().split()))
  for i in row:
    carr.append(i)

all = 9 * 8 * 7
sad_count = 0

p = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8], 9)


for case in p:
  for space in case:
    i = space // 3
    j = space % 3


print(sad_count / all)
