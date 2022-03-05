s = input()
q = int(input())

def f(root, rest):
    if root == 'A':
        if rest:
            return 'C'
        else:
            return 'B'
    elif root == 'B':
        if rest:
            return 'A'
        else:
            return 'C'
    else:
        if rest:
            return 'B'
        else:
            return 'A'

def add(s, i):
    if s == 'A':
        if i == 0:
            return 'A'
        elif i == 1:
            return 'B'
        else:
            return 'C'
    elif s == 'B':
        if i == 0:
            return 'B'
        elif i == 1:
            return 'C'
        else:
            return 'A'
    elif s == 'C':
        if i == 0:
            return 'C'
        elif i == 1:
            return 'A'
        else:
            return 'B'

def get_rest(n):
    for i in range(3):
        s = str(n-i)
        sum = 0
        for j in range(len(s)):
            sum += int(s[j])
        if sum % 3 == 0:
            return i

def explore(t, k):
    rest = k % 2
    if t == 0:
        return s[k]
    if k == 0:
        t = get_rest(t)
        return add(s[0], t)
    parent = explore(t-1, k//2)
    return f(parent, rest)

for i in range(q):
    t, k = list(map(int, input().split()))
    k -= 1
    print(explore(t, k))
