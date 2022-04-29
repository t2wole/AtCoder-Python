def f(t):
    return t**2 + 2*t + 3

t = int(input())
result = f(f(f(t) + t) + f(f(t)))
print(result)
