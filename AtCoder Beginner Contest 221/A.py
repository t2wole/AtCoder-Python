a, b = map(int, input().split())

if a-b == 0:
    print(1)
else:
    print(32 ** (a-b))
    