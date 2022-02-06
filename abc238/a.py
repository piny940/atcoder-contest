import numpy as np


n = int(input())
if n > 2 * np.log2(n):
    print("Yes")
else:
    print("No")
