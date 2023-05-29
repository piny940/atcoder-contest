import math

AL_COUNT = 26


def char_to_int(char):
  return ord(char) - 97


def int_to_char(int):
  return chr(int + 97)


s = input()
t = input()

scounts = [0] * AL_COUNT
tcounts = [0] * AL_COUNT

sat_count = 0
tat_count = 0

for i in range(len(s)):
  if s[i] == '@':
    sat_count += 1
    continue
  scounts[char_to_int(s[i])] += 1
for i in range(len(t)):
  if t[i] == '@':
    tat_count += 1
    continue
  tcounts[char_to_int(t[i])] += 1

ans = True
for i in range(AL_COUNT):
  if scounts[i] == tcounts[i]:
    continue
  if int_to_char(i) in 'atcoder':
    if scounts[i] > tcounts[i]:
      tat_count -= scounts[i] - tcounts[i]
    else:
      sat_count -= tcounts[i] - scounts[i]
    if sat_count < 0 or tat_count < 0:
      ans = False
      break
    continue
  ans = False
  break

print('Yes' if ans else 'No')
