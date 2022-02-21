n = int(input())

arr = list(map(int, input().split()))

vs = []
for a in arr:
    if a not in vs:
        vs.append(a)

print(len(vs))
