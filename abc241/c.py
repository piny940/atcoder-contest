n = int(input())
srr = []

for i in range(n):
    srr.append(input())

ans = False

for i in range(n):
    if ans:
        break
    for j in range(n-5):
        # 横方向
        hor = 0

        # 縦方向
        ver = 0
        for k in range(6):
            if srr[i][j+k] == '#':
                hor += 1
            if srr[j+k][i] == '#':
                ver += 1
        if hor >= 4 or ver >= 4:
            ans = True
            break

for i in range(n-5):
    if ans:
        break

    for j in range(n-5):
        # 左上から右下へ
        num1 = 0
        # 左下から右上へ
        num2 = 0
        for k in range(6):
            if srr[i+k][j+k] == '#':
                num1 += 1
            if srr[i+5-k][j+k] == '#':
                num2 += 1
        
        if num1 >= 4 or num2 >= 4:
            ans = True
            break

if ans:
    print('Yes')
else:
    print('No')
