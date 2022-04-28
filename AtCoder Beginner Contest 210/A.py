n, a, x, y = list(map(int, input().split()))

if n <= a:
    print(x * n)
else:
    print(a * x + (n-a) * y)

