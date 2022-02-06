T = int(input())

def get_and(x, y):
    if x == '1' and y == '1':
        return '1'
    else:
        return '0'


for i in range(T):
    a, s = map(int, input().split())
    a1 = format(a, 'b')
    s1 = format(s, 'b')
    if s < a:
        print('No')
        continue
    elif len(s1) > len(a1):
        for j in range(len(s1) - len(a1)):
            a1 = '0' + a1
    s1 = '0' + s1

    x = ''
    y = ''
    able = True
    tmp = '0'
    j = 1
    while True:
        if j == len(s1):
            if tmp == s1[-j]:
                print('Yes')
            else:
                print('No')
            break
        
        if s1[-j] != tmp:
            x = '1' + x
            y = '0' + y
            if a1[-j] == '1':
                print('No')
                break
        elif a1[-j] == '1':
            x = '1' + x
            y = '1' + y
            tmp = '1'
        else:
            x = '0' + x
            y = '0' + y
            tmp = '0'
        
        j += 1
