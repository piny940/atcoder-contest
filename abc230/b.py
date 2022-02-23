s = input()

t = 'oxx' * (10 ** 5)

ans = False

for i in range(len(t) - len(s) + 1):
    if s == t[i:i+len(s)]:
        ans = True
        break
    
if ans:
    print('Yes')
else:
    print('No')
