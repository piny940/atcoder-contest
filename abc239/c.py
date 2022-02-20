def around(x, y):
    return [(x+1, y+2),
            (x+1, y-2),
            (x+2, y+1),
            (x+2, y-1),
            (x-1, y+2),
            (x-1, y-2),
            (x-2, y+1),
            (x-2, y-1)]

x1, y1, x2, y2 = list(map(int, input().split()))

around1 = around(x1, y1)
around2 = around(x2, y2)

ans = False

for coord in around1:
    if coord in around2:
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')
