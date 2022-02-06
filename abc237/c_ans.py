s = input()

n = len(s)

x = y = 0
for i in range(n):
    if s[i] == 'a':
        x += 1
    else:
        break

for i in reversed(range(n)):
    if s[i] == 'a':
        y += 1
    else:
        break

if x == n:
    print('Yes')
    exit()

if x > y:
    print('No')
    exit()

new = s[x:n-y]
re = new[::-1]

if new == re:
    print('Yes')
else:
    print('No')
