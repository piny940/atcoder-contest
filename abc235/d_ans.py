from collections import deque


a, n = map(int, input().split())

m = 1
while m <= n:
    m *= 10

d = [-1] * m
q = deque()
q.append(1)
d[1] = 0

while len(q):
    c = q.popleft()
    opt1 = c * a
    if opt1 < m and d[opt1] == -1:
        q.append(opt1)
        d[opt1] = d[c] + 1
        
    if c >= 10 and c % 10 != 0:
        s = str(c)
        opt2 = int(s[-1:] + s[:-1])
        if opt2 < m and d[opt2] == -1:
            q.append(opt2)
            d[opt2] = d[c] + 1
            
print(d[n])
