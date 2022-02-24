n, l = list(map(int, input().split()))
k = int(input())
arr = list(map(int, input().split()))
brr = []

tmp = 0
for cut in arr:
    brr.append(cut - tmp)
    tmp = cut
brr.append(l - tmp)

max = l
min = 1

while min != max:
    avg = (max + min) // 2 + 1
    sum = 0
    count = 0
    for i in range(n+1):
        sum += brr[i]
        if sum >= avg:
            sum = 0
            count += 1
    if count < k + 1:
        max = avg - 1
    else:
        min = avg

print(max)
