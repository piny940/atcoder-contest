n = int(input())
s = input()

heights = [1] * n

for i in range(n - 1):
  if s[i] == 'A':
    heights[i + 1] = heights[i] + 1
  else:
    if heights[i] > 1:
      heights[i + 1] = 1
    else:
      heights[i + 1] = 1
      j = i
      while True:
        heights[j] += 1
        if j == 0 or heights[j - 1] != heights[j]:
          break
        j -= 1

print(sum(heights))
