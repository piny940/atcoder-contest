n, q = list(map(int, input().split()))

arr = list(map(int, input().split()))

nums_dict = {}

for i in range(n):
    if arr[i] not in nums_dict:
        nums_dict[arr[i]] = [i + 1]
    else:
        nums_dict[arr[i]].append(i + 1)

for i in range(q):
    x, k = list(map(int, input().split()))
    if x not in nums_dict or len(nums_dict[x]) < k:
        print(-1)
    else:
        print(nums_dict[x][k-1])
