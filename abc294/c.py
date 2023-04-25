n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

count = 1

answer_a = []
answer_b = []

a_index = 0
b_index = 0

while a_index < len(arr) and b_index < len(brr):
  if arr[a_index] < brr[b_index]:
    answer_a.append(count)
    count += 1
    a_index += 1
  else:
    answer_b.append(count)
    count += 1
    b_index += 1

while a_index < len(arr):
  answer_a.append(count)
  a_index += 1
  count += 1

while b_index < len(brr):
  answer_b.append(count)
  b_index += 1
  count += 1

print(*answer_a)
print(*answer_b)
