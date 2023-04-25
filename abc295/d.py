def to_bin(n: int, width: int = -1):
  if width > 0:
    return bin(n)[2:].zfill(width)
  else:
    return bin(n)[2:]

s = input()

answer = 0

counts = [0] * 2**10

actual = list('0000000000')
counts[0] += 1
for s_char in s:
  actual[int(s_char)] = '0' if actual[int(s_char)] == '1' else '1'
  str_actual = ''.join(actual)
  counts[int(str_actual, 2)] += 1

for pattern in range(2 ** 10):
  count = counts[pattern]

  answer += count * (count - 1) // 2

print(answer)
