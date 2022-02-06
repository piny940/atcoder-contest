from collections import deque


n = int(input())
s = input()

a = deque([n])
prv = 0

for i in reversed(range(n)):
    if s[i] == 'L':
        a.append(i)
    else:
        a.appendleft(i)
print(*a)
