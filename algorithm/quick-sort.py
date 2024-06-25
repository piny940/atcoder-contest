from copy import copy

original = [5, 6, 1, 2, 3, 4, 7, 8, 9, 10, 2, 4, 6, 8, 10, 3, 5, 7, 9, 1, 2, 4, 6, 8, 10]
# original = [2, 2, 2]

def sort_rec(arr, start, end):
  if end - start <= 1:
    return
  mid = arr[start]

  l = start
  r = end - 1
  while l < r:
    while arr[r] >= mid and l < r:
      r -= 1
    while arr[l] < mid and l < r:
      l += 1
    arr[l], arr[r] = arr[r], arr[l]
  
  sort_rec(arr, start, r+1)
  sort_rec(arr, r+1, end)

def sort(arr):
  sort_rec(arr, 0, len(arr))

arr = copy(original)
sort(arr)
# print(arr)
print(arr)
