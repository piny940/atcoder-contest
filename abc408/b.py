n = int(input())
arr = list(map(int, input().split()))
s = set(arr)
l = list(s)
l.sort()

print(len(l))
print(' '.join(map(str, l)))
