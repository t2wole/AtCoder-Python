a, b, c = list(map(int, input().split()))
sum = a + b + c
print(sum - min(a, b, c))
