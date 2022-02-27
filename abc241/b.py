n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))


ans = True

for i in range(m):
    if brr[i] in arr:
        arr.remove(brr[i])
    else:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')
