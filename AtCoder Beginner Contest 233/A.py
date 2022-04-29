import math
x, y = map(int, input().split())

if y > x:
    print(math.ceil((y - x) / 10))
else:
    print(0)
    