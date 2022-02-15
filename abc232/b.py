import string

alphs = list(string.ascii_lowercase)

s = list(input())
t = list(input())

t0idx = alphs.index(t[0])
s0idx = alphs.index(s[0])

if t0idx >= s0idx:
    k = t0idx - s0idx
else:
    k = len(alphs) + t0idx - s0idx

alphs.extend(alphs)

ans = True

for i in range(len(s)):
    if alphs[alphs.index(s[i]) + k] != t[i]:
        ans = False
        break
    
if ans:
    print('Yes')
else:
    print('No')
