n = int(input())

hrr = list(map(int, input().split()))

p = 0

while p+1 < len(hrr) and hrr[p] < hrr[p + 1]:
    p += 1

print(hrr[p])
