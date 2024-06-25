import math, copy

original = [5, 2, 4, 6, 1, 3, 2, 6, 4, 5, 7, 8, 9, 10, 3, 1, 2, 4, 5, 6, 7, 8, 9, 10]
arr = copy.copy(original)

def heapify(arr, i):
  li = 2 * i + 1
  ri = 2 * i + 2
  l = arr[li] if li < len(arr) else -math.inf
  r = arr[ri] if ri < len(arr) else -math.inf
  if arr[i] >= l and arr[i] >= r:
    return
  if l >= r:
    arr[i], arr[li] = l, arr[i]
    heapify(arr, li)
  else:
    arr[i], arr[ri] = r, arr[i]
    heapify(arr, ri)

def build_heap(arr):
  for root in range(len(arr)//2 - 1, -1, -1):
    heapify(arr, root)

def valid_heap(arr):
  for root in range(0, len(arr)//2):
    l = arr[2 * root + 1] if 2 * root + 1 < len(arr) else -math.inf
    r = arr[2 * root + 2] if 2 * root + 2 < len(arr) else -math.inf
    if arr[root] < l or arr[root] < r:
      return False
  return True

def pop(arr: list[int]):
  if len(arr) == 1:
    return arr.pop()
  head = arr[0]
  arr[0] = arr[-1]
  arr.pop()
  heapify(arr, 0)
  return head

def insert(arr: list[int], v):
  arr.append(v)
  current = len(arr) - 1
  while True:
    if current == 0:
      return
    parent = (current-1) // 2
    if arr[parent] >= arr[current]:
      return
    arr[parent], arr[current] = arr[current], arr[parent]
    current = parent

def equal(arr1, arr2):
  count1, count2 = {}, {}
  for a in arr1:
    if count1.get(a) == None:
      count1[a] = 1
    else:
      count1[a] += 1
  for b in arr2:
    if count2.get(b) == None:
      count2[b] = 1
    else:
      count2[b] += 1
  return count1 == count2
  

print(valid_heap(arr))
build_heap(arr)
print(valid_heap(arr))
print(arr)
sorted = sorted(arr, reverse=True)
to_remove = copy.copy(arr)
for i in range(len(to_remove)):
  head = pop(to_remove)
  if head != sorted[i]:
    print('sort err!')

to_build = []
for a in original:
  insert(to_build, a)

print(valid_heap(to_build))
print(equal(original, to_build))
