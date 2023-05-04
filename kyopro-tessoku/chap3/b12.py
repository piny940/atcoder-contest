n = int(input())

def f(x):
  return x ** 3 + x

start = 0
end = 100

while end - start > 0.001:
  middle = (start + end) / 2
  if f(middle) > n:
    end = middle
  else:
    start = middle

print(start)
