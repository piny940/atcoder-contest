from collections import deque


n = int(input())

if n >= 42:
    n += 1

srr = deque(list(str(n)))

while len(srr) < 3:
    srr.appendleft('0')

srr = ''.join(list(srr))

print(f'AGC{srr}')
