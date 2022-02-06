n, m = list(map(int, input().split()))
srr = input().split()
trr = set(input().split())

for name in srr:
    if name in trr:
        print('Yes')
    else:
        print('No')
