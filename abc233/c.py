n, x = list(map(int, input().split()))
larr = []
for i in range(n):
    larr.append(list(map(int, input().split())))

product = 1

class Explore:
    def __init__(self):
        self.ans = 0
    
    def explore(self, bag_num, tmp):
        for j in range(1, larr[bag_num-1][0] + 1):
            tmp2 = tmp * larr[bag_num-1][j]
            if tmp2 > x:
                continue
            
            if bag_num == n:
                if tmp2 == x:
                    self.ans += 1
            else:
                self.explore(bag_num+1, tmp2)

ex = Explore()
ex.explore(1, product)
print(ex.ans)
