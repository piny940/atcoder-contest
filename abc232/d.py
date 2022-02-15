from collections import deque


h, w = list(map(int, input().split()))

crr = []
for i in range(h):
    crr.append(list(input()))

to_search = deque([])
to_search.append((0, 0))
ans = 0

while to_search:
    for i in range(len(to_search)):
        current = to_search[0]
        to_search.popleft()
        
        # right side
        right = (current[0] + 1, current[1])
        if (right[0] < len(crr[0])) and (crr[right[1]][right[0]] == '.') and (right not in to_search):
            to_search.append(right)
        
        # down side
        down = (current[0], current[1] + 1)
        if (down[1] < len(crr)) and (crr[down[1]][down[0]] == '.') and (down not in to_search):
            to_search.append(down)
    ans += 1

print(ans)
