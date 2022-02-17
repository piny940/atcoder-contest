n = int(input())

votes = {}
names = []

for i in range(n):
    s = input()
    if s in votes:
        votes[s] += 1
    else:
        votes[s] = 1
        names.append(s)

ans = ''
tmp = 0

for name in names:
    if tmp < votes[name]:
        ans = name
        tmp = votes[name]

print(ans)
