a, b, c = map(int, input().split())

result = 0

for i in range(a, b + 1):
    if i % c == 0:
        result = i
        break
    else:
        result = -1
print(result)
