n = int(input())

if n % 2 != 0:
    exit()

def explore(arr, diff):
    if len(arr) == n-1:
        if diff == 1:
            arr.append(')')
            diff -= 1
            print(''.join(arr))
        
        return
    
    arr1 = arr + ['(']
    diff1 = diff + 1
    explore(arr1, diff1)
    
    if diff > 0:
        arr2 = arr + [')']
        diff2 = diff - 1
        explore(arr2, diff2)

explore([], 0)
