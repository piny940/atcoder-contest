import string
import numpy as np


a, n = list(map(int, input().split()))

process_counter = 0

def proceed(m0):
    '''
    m0 is expected to be able to be divided by a
    '''
    count = 0
    mst = str(m0)
    digits_num = len(mst)
    able = False

    if m0 == 1:
        return 0
    
    for i in range(digits_num):
        if i == 0 : 
            if m0 % a == 0 and proceed(m0 // a) != -1:
                able = True
                count = 1 + proceed(m0 // a)
        elif digits_num > 1:
            if mst[-i] == '0':
                continue
            m1 = int(mst[-i:] + mst[:-i])
            if m1 % a == 0 and proceed(m1 // a) != -1:
                if able:
                    count = min(count, i + proceed(m1 // a))
                else:
                    able = True
                    count = i + 1 + proceed(m1 // a)
    
    return count if able else -1

print(proceed(n))
