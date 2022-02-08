from curses import use_default_colors
import numpy as np

n = int(input())
used = np.zeros(20)
vec = []
arr = []
for i in range(2 * n-1):
    li = list(map(int, input().split()))
    arr.append(li)
    

def calc():
    if len(vec) == n:
        ret = 0
        
